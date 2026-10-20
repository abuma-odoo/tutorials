from odoo import fields, models

class Plant(models.Model):
    _name = "plant_shop"
    _description = "plant shop items"

    name = fields.Char(required=True)
    description = fields.Text()
    price = fields.Float(required=True)

    category_id = fields.Many2one("plant_categories", string="Category")