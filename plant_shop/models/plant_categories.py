from odoo import fields, models

class Category(models.Model):
    _name = "plant_categories"

    name = fields.Char(required=True)