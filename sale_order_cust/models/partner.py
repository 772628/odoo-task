from odoo import api, models, fields, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'


    is_distributor = fields.Boolean(string="Distributor",)
    is_default_distributor = fields.Boolean(string="Default Distributor",)

    @api.onchange('is_default_distributor')
    def _onchange_is_default_distributor(self):
        check_partner_id = self.env['res.partner'].search([('is_default_distributor','=','t')], limit=1)
        if check_partner_id:
            raise UserError(_(check_partner_id.name + ' Already Set As Default Distributor'))
