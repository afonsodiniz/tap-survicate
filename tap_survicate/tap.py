"""Survicate tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th

from tap_survicate import streams


class TapSurvicate(Tap):
    """Survicate tap class."""

    name = "tap-survicate"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_url",
            th.StringType,
            default="https://data-api.survicate.com/v2/",
            description="The url for the API service",
        ),
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,
            description="The token to authenticate against the API service",
        )
    ).to_dict()

    def discover_streams(self) -> list[streams.SurvicateStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.SurveysStream(self)
        ]


if __name__ == "__main__":
    TapSurvicate.cli()
