"""Stream type classes for tap-survicate."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_survicate.client import SurvicateStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources

SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"


class SurveysStream(SurvicateStream):
    """Stream for Surveys endpoint"""

    name = "surveys"
    path = "/surveys.json"
    primary_keys = ["id"]

    schema_filepath = SCHEMAS_DIR / "surveys.json"  # noqa: ERA001
