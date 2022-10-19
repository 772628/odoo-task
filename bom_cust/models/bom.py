from odoo import api, models, fields, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'mrp.bom.line'

    time_as = fields.Float("Minuts")

    @api.onchange('product_id')
    def _find_product_time(self):
        for rec in self:
            product = self.env['mrp.bom'].search([('product_id','=',rec.product_id.id)],limit=1)
            rec.time_as = round(product.time_total * 60)

class ResPartner(models.Model):
    _inherit = 'mrp.bom'



    @api.depends('bom_line_ids.time_as')
    def _estimate_time(self):
        final_time = 0.0
        for rec in self:
            for time in self.bom_line_ids:
                final_time += time._origin.time_as
            rec._origin.update({
                'time_total' : final_time / 60,
                })

    time_total = fields.Float("Total Estimate Time(Hours)", store=True, readonly=True,compute="_estimate_time")