from odoo import models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_open_ai_wizard(self):
        self.ensure_one()
        return {
            'name': 'Generate AI Description',
            'type': 'ir.actions.act_window',
            'res_model': 'ai.description.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_product_tmpl_id': self.id},
        }
