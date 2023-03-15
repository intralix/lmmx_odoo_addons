# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    lmmx_hub_api_id = fields.Char(
        string=_("HUB API Id"),
        config_parameter='lmmx.hub_api_id'
    )

    lmmx_hub_api_secret = fields.Char(
        string=_("HUB API Secret"),
        config_parameter='lmmx.hub_api_secret'
    )

    lmmx_hub_api_basic_token = fields.Char(
        string=_("HUB API Basica Token"),
        config_parameter='lmmx.hub_api_basic_token'
    )

    lmmx_hub_api_login_url = fields.Char(
        string=_("HUB API Login Url"),
        config_parameter='lmmx.hub_api_login_url'
    )

    lmmx_hub_api_invoice_url = fields.Char(
        string=_("HUB API Invoice Url"),
        config_parameter='lmmx.hub_api_invoice_url'
    )

    lmmx_hub_api_grant_type = fields.Selection(
        [
            ('client_credentials', _('Client Credentials')),
            ('authorization_code', _('Authorization Code')),
            ('refresh_token', _('Refresh Token')),
        ],
        default='client_credentials',
        string=_("HUB API Login Url"),
        config_parameter='lmmx.hub_api_grant_type'
    )

    def set_values(self):
        return super(ResConfigSettings, self).set_values()

    @api.model
    def get_values(self):
        return super(ResConfigSettings, self).get_values()

