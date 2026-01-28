"""Config flow for Simple HTTP Client integration."""
from __future__ import annotations

from typing import Any

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class SimpleHttpClientConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Simple HTTP Client."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        # Check if already configured
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            # Create the entry with no configuration data
            return self.async_create_entry(
                title="Simple HTTP Client",
                data={},
            )

        # Show the configuration form (empty form, just confirmation)
        return self.async_show_form(step_id="user")
