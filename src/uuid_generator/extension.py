from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class UuidGenerator(Extension):
    """UUID v4/v7 generator and batch insertion tool"""

    def __init__(self, api: "ExtensionsAPI") -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("UUID Generator extension initialised.")

    def install(self) -> None:
        """Run when extension is loaded."""
        self.api.logger.info("UUID Generator installed successfully.")
