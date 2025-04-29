"""Config flow to configure Heos."""

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.components.heos.config_flow import HeosFlowHandler
from homeassistant.core import callback
from homeassistant.helpers import selector

from .const import (
    CONF_FORCE_EXTERNAL_POWER,
    CONF_PASSWORD,
    CONF_USERNAME,
    CONF_VOLUME_CONTROL,
    DOMAIN,
    VOLUME_CONTROL_EXTERNAL,
    VOLUME_CONTROL_INTERNAL,
)

DEFAULT_OPTIONS = {
    CONF_FORCE_EXTERNAL_POWER: True,
    CONF_VOLUME_CONTROL: VOLUME_CONTROL_EXTERNAL,
    CONF_USERNAME: "",
    CONF_PASSWORD: "",
}


class OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_VOLUME_CONTROL,
                        default=DEFAULT_OPTIONS[CONF_VOLUME_CONTROL],
                    ): vol.In([VOLUME_CONTROL_INTERNAL, VOLUME_CONTROL_EXTERNAL]),
                    vol.Required(
                        CONF_FORCE_EXTERNAL_POWER,
                        default=DEFAULT_OPTIONS[CONF_FORCE_EXTERNAL_POWER],
                    ): bool,
                    vol.Optional(
                        CONF_USERNAME, default=DEFAULT_OPTIONS[CONF_USERNAME]
                    ): selector.TextSelector(),
                    vol.Optional(
                        CONF_PASSWORD, default=DEFAULT_OPTIONS[CONF_PASSWORD]
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.PASSWORD
                        )
                    ),
                }
            ),
        )


class ACTHeosFlowHandler(HeosFlowHandler, domain=DOMAIN):
    """Define a flow for HEOS."""

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return OptionsFlowHandler(config_entry)
