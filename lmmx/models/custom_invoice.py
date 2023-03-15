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

    # def button_publish_at_portal(self):
    #     self._cron_sync_invoices_to_hub()

        # _logger.info('We pressed the button successfully')
        # if not self.published_in_portal:
        #     _logger.warning('Active Model %s', self.id)
        #     attachments = self.env['ir.attachment'].search(
        #         [('res_model', '=', 'account.move'), ('res_id', '=', self.id)])
        #     for attachment in attachments:
        #         # _logger.warning('Account ID: %s', self.partner_id.id)
        #         # _logger.warning('Account Name: %s', self.partner_id.name)
        #         # _logger.warning('Invoice Date: %s', self.invoice_date)
        #         # _logger.warning('Created At: %s', self.create_date.date())
        #         # _logger.warning('Attachment ID: %s', attachment.id)
        #         # _logger.warning('Attachment Name: %s', attachment.name)
        #         # _logger.warning('Attachment Mime Type: %s', attachment.mimetype)
        #         # _logger.warning('Attachment Res Model: %s', attachment.res_model)
        #         # _logger.warning('Attachment Res Name: %s', attachment.res_name)
        #         values = {
        #             "invoicedAt": self.invoice_date.strftime("%Y-%m-%d"),
        #             "odooAccountId": self.partner_id.id,
        #         }
        #
        #         pdf_file = {'invoice': (attachment.name,  base64.b64decode(attachment.datas), 'application/pdf', {'Expires': '0'})}
        #
        #         self.login_to_external_api(values, pdf_file)
        #
        # else:
        #     _logger.error('Already Published at HUB Portal')
        #     raise UserError(_("Already Published at HUB Portal"))

    # def login_to_external_api(self, values, pdf_file):
    #
    #     lmmx_config = self.sudo().env['ir.config_parameter']
    #     lmmx_hub_api_basic_token = lmmx_config.get_param('lmmx.hub_api_basic_token')
    #     lmmx_hub_api_login_url = lmmx_config.get_param('lmmx.hub_api_login_url')
    #     lmmx_hub_api_grant_type = lmmx_config.get_param('lmmx.hub_api_grant_type')
    #
    #     post_headers = {
    #         "Authorization": "Basic "+lmmx_hub_api_basic_token,
    #         "Content-Type": "application/x-www-form-urlencoded"
    #     }
    #
    #     payload = {'grant_type': lmmx_hub_api_grant_type}
    #     r = requests.post(lmmx_hub_api_login_url, headers=post_headers, data=payload)
    #     if r.status_code == requests.codes.ok:
    #         _logger.warning('API Response Headers %s', r.headers)
    #         _logger.warning('API Response %s', r.text)
    #         _logger.warning('Request Object %s', r)
    #         try:
    #             resp_dict = r.json()
    #             access_token = resp_dict.get('access_token')
    #             # _logger.error('API Response access_token %s', access_token)
    #             expires_in = resp_dict.get('expires_in')
    #             # _logger.error('API Response expires_in %s', expires_in)
    #             token_type = resp_dict.get('token_type')
    #             # _logger.error('API Response token_type %s', token_type)
    #             access_token_at = resp_dict.get('access_token')
    #             # _logger.error('API Response access_token_at %s', access_token_at)
    #         except JSONDecodeError:
    #             raise UserError(_("Json Decode Error on API Call."))
    #
    #         # attempt to send file to Endpoint
    #         _logger.error('Trying to SEND PDF..........')
    #         lmmx_hub_api_invoice_url = lmmx_config.get_param('lmmx.hub_api_invoice_url')
    #         post_headers = {"Authorization": "Bearer " + access_token}
    #
    #         _logger.warning('HEADERS: %s', post_headers)
    #         _logger.warning('DATA: %s', values)
    #         _logger.warning('PDF: %s', pdf_file)
    #
    #         r = requests.post(lmmx_hub_api_invoice_url, headers=post_headers, data=values, files=pdf_file)
    #         _logger.error('API REQUEST Made ....................')
    #         _logger.error('API Response Status Code %s', r.status_code)
    #
    #         if r.status_code == 201:
    #             _logger.warning('API Response Headers %s', r.headers)
    #             _logger.warning('API Response %s', r.text)
    #             _logger.warning('Request Object %s', r)
    #             self.write({
    #                 'published_in_portal': True
    #             })
    #
    #             try:
    #                 resp_dict = r.json()
    #                 _logger.warning('Request Object %s', resp_dict)
    #
    #             except JSONDecodeError:
    #                 raise UserError(_("Json Decode Error on API Call."))
    #         else:
    #             _logger.error('There was an API Error %s', r.text)
    #     else:
    #         _logger.error('There was an API Error %s', r.text)

    # @api.model
    # def _cron_sync_invoices_to_hub(self):
    #     """
    #         Sync Invoices to External HUB Platform
    #     """
    #     _logger.warning('Running the invoice synchronizer to the HUB platform :: Company %s', self.company_id)
    #     invoices = self.sudo().env['account.move'].search([
    #         ('move_type', 'in', ['out_invoice', 'out_refund']),
    #         ('state', '=', 'posted'),
    #         ('published_in_portal', '=', False),
    #         # ('l10n_mx_edi_sat_status', '=', 'valid')
    #         ('company_id', '=', self.company_id.id)
    #     ])
    #
    #     _logger.warning('Invoices: %s', invoices)
    #
    #     # Iterate records in this configuration
    #     for invoice in invoices:
    #         _logger.info('---------------------------------------------------------------------------------')
    #         _logger.error('Invoice: %s', invoice.with_company(invoice.company_id).name)
    #         _logger.info('---------------------------------------------------------------------------------')
    #         attachments = self.env['ir.attachment'].search([
    #             ('res_model', '=', 'account.move'),
    #             ('res_id', '=', self.id),
    #             ('mimetype', '=', 'application/pdf'),
    #         ])
    #
    #         for attachment in attachments:
    #             _logger.warning('Attachment ID: %s', attachment.id)
    #             _logger.warning('Attachment Name: %s', attachment.name)
    #             _logger.warning('Attachment Mime Type: %s', attachment.mimetype)
    #             _logger.warning('Attachment Res Model: %s', attachment.res_model)
    #             _logger.warning('Attachment Res Name: %s', attachment.res_name)
    #             _logger.info('---------------------------------------------------------------------------------')
    #             # Gather info
    #             values = {
    #                 "invoicedAt": self.invoice_date.strftime("%Y-%m-%d"),
    #                 "odooAccountId": self.partner_id.id,
    #             }
    #             pdf_file = {'invoice': (attachment.name,  base64.b64decode(attachment.datas), 'application/pdf', {'Expires': '0'})}
    #             self.login_to_external_api(values, pdf_file)
    #     return
