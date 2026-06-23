from odoo import models


class ClinicConsultation(models.Model):
    _inherit = "clinic.consultation"

    def _dispense_prescription(self):
        """Dispense against real Odoo Inventory when the medicine is linked to a
        product; otherwise fall back to the simple on-hand counter from clinic."""
        self.ensure_one()
        stock_location = self.env.ref('stock.stock_location_stock', raise_if_not_found=False)
        for line in self.prescription_line_ids:
            medicine = line.medicine_id
            if not medicine or not line.quantity:
                continue
            if medicine.product_id and stock_location:
                self.env['stock.quant']._update_available_quantity(
                    medicine.product_id, stock_location, -line.quantity
                )
            else:
                medicine.qty_available -= line.quantity
