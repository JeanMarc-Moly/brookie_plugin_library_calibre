from unittest.case import TestCase

from pydantic import parse_obj_as
from pydantic.error_wrappers import ValidationError

from brookie_plugin_library_calibre import Calibre


class TestParse(TestCase):
    def test_with_valid_folder_path(self):
        try:
            parse_obj_as(
                Calibre, dict(name="books", plugin="calibre", path="resource/calibre"),
            )
        except Exception:
            self.fail("Unable to setup calibre plugin")

    def test_with_valid_full_path(self):
        try:
            parse_obj_as(
                Calibre,
                dict(
                    name="books", plugin="calibre", path="resource/calibre/metadata.db"
                ),
            )
        except Exception:
            self.fail("Unable to setup calibre plugin")

    def test_with_invalid_folder_path(self):
        with self.assertRaises(ValidationError):
            parse_obj_as(
                Calibre, dict(name="books", plugin="calibre", path="resource/invalid"),
            )

    def test_with_invalid_full_path(self):
        with self.assertRaises(ValidationError):
            parse_obj_as(
                Calibre,
                dict(
                    name="books", plugin="calibre", path="resource/calibre/invalid.db"
                ),
            )
