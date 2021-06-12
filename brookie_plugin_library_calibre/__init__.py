from contextlib import asynccontextmanager
from dataclasses import InitVar, dataclass, field
from io import BytesIO
from pathlib import Path
from typing import AsyncGenerator, BinaryIO, ClassVar, Literal

from brookie_plugin_library_abstract import Library
from brookie_plugin_library_abstract.util import Archive
from databases import Database, DatabaseURL


@dataclass
class Calibre(Library):

    DB_PROTOCOL: ClassVar[str] = "sqlite"
    DB_FILE: ClassVar[Path] = Path("metadata.db")
    COVER: ClassVar[Path] = Path("cover.jpg")

    name: str
    path: InitVar[Path]
    database: Database = field(init=False)
    plugin: Literal["calibre"]

    def __post_init__(self, path: Path):
        if not path.is_dir():
            path = path / self.DB_FILE
        if not path.exists():
            raise ValueError(f"No db file at {path}")

        url = DatabaseURL(f"{self.DB_PROTOCOL}:///{path}")
        self.database = Database(url)

    async def __aenter__(self) -> "Calibre":
        await self.database.connect()
        return self

    async def __aexit__(self) -> None:
        await self.database.disconnect()

    async def get_book_cover(self, book_id: int) -> BinaryIO:
        b = await self._get_book_path(book_id)
        with (b.parent / self.COVER).open("rb") as c:
            return c

    async def get_book_pages(self, book_id: int) -> AsyncGenerator[str, None]:
        async with self._get_archive(book_id) as a:
            async for p in Archive.get_book_pages(a):
                yield p

    async def get_book_page(self, book_id: int, page_id: int) -> BytesIO:
        async with self._get_archive(book_id) as a:
            return Archive.get_book_page(a, page_id)

    @asynccontextmanager
    async def _get_archive(self, id_: int) -> AsyncGenerator[BinaryIO, None]:
        with (await self._get_book_path(id_)).open("rb") as b:
            yield b

    async def _get_book_path(self, id_: int) -> Path:
        r = await self.database.fetch_one(
            """
            SELECT path, name, format
            FROM (SELECT * FROM books WHERE id = :id) b
            JOIN data AS d ON b.id = d.book
            """,
            dict(id=id_),
        )
        if r is None:
            raise Exception(f"Book {id_} does not exist")
        path, name, ext = r
        return Path(f"{self.path / path / name}.{ext.lower()}")


__all__ = ["Calibre"]
