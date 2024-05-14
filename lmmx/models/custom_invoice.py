from odoo import api, models, fields, _
from odoo.exceptions import UserError
import logging
import requests
from json import JSONDecodeError
import base64
_logger = logging.getLogger(__name__)


class CustomInvoice(models.Model):
    _inherit = 'account.move'

    published_in_portal = fields.Boolean(
        string=_("Published in Portal"),
        default=False
    )
