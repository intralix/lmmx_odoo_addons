from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)


class CustomRepair(models.Model):
    _inherit = 'repair.order'

    reparation_type = fields.Selection(
        [
            ('repair', _('Repair')),
            ('warranty', _('Warranty')),
            ('diagnosis', _('diagnosis')),
        ],
        default="repair",
        required=True,
    )