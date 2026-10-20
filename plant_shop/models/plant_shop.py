from odoo import api, fields, models

class Plant(models.Model):
    _name = "plant_shop"
    _description = "plant shop items"

    name = fields.Char(required=True)
    description = fields.Text()
    price = fields.Float(required=True)
    discount = fields.Float(compute="_compute_total")

    category_id = fields.Many2one("plant_categories", string="Category")

    @api.depends("price")
    def _compute_total(self):
        for record in self:
            record.discount = record.price * 0.50

    @api.onchange("category_id")
    def _onchange_category_id(self):
        self.name = "A type of %s" % (self.category_id.name)