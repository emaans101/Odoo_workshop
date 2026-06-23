from odoo import models, fields


class ClinicMedicine(models.Model):
    _inherit = "clinic.medicine"

    product_id = fields.Many2one(
        "product.product",
        string="Inventory Product",
        help="Link to an Inventory product to dispense against real stock moves.",
    )
