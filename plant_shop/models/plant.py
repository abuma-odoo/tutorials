from odoo import fields, models

class Plant(models.Model):
    _name = "plant"
    _description = "plant shop items"

    name = fields.Char(required=True)
    description = fields.Text()
    price = fields.Float(required=True)