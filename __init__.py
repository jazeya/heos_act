"""Denon HEOS Media Player."""
import homeassistant.components.heos.__init__
from homeassistant.components.heos.__init__ import (
    async_setup,  # noqa: F401
    async_setup_entry,  # noqa: F401
    async_unload_entry,  # noqa: F401
)

from .const import DOMAIN

homeassistant.components.heos.__init__.DOMAIN = DOMAIN
