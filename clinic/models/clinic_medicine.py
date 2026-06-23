from odoo import models, fields


class ClinicMedicine(models.Model):
    _name = "clinic.medicine"
    _description = "Medicine / Medical Supply"
    _order = "name"

    name = fields.Char(required=True)
    reference = fields.Char(string="Code")

    price = fields.Float(string="Unit Price")

    qty_available = fields.Float(string="Quantity On Hand", default=0.0)