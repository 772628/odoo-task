from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'sale.order'

    dist_partner_id = fields.Many2one('res.partner',string="Distributor")

