from unittest.case import TestCase

from pydantic import parse_obj_as

from brookie_plugin_library_calibre import Calibre


class TestParse(TestCase):
    def test_parsing(self):
        try:
            parse_obj_as(
                Calibre, dict(name="books", plugin="calibre", path="resource/calibre"),
            )
        except Exception:
            self.fail("Unable to setup calibre plugin")
