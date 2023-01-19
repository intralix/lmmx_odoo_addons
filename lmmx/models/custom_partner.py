from odoo import api, models, fields, _


class CustomPartner(models.Model):
    _inherit = 'res.partner'

    client_category = fields.Selection(
        [
            ('a', _('A')),
            ('b', _('B')),
            ('c', _('C')),
            ('d', _('D')),
        ],
        string=_("Client Category")
    )
