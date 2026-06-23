from odoo import models, fields


class ClinicConsultation(models.Model):
    _inherit = "clinic.consultation"

    consultation_fee = fields.Float(string="Consultation Fee", default=20.0)
    invoice_id = fields.Many2one("account.move", string="Invoice", readonly=True, copy=False)

    def action_done(self):
        res = super().action_done()
        for record in self:
            if not record.invoice_id:
                record._create_invoice()
        return res

    def _create_invoice(self):
        self.ensure_one()
        partner = self.patient_id._ensure_billing_partner()
        invoice_lines = [
            fields.Command.create({
                "name": "Consultation - %s" % (self.doctor_id.name or ""),
                "quantity": 1,
                "price_unit": self.consultation_fee,
            })
        ]
        for line in self.prescription_line_ids:
            invoice_lines.append(fields.Command.create({
                "name": line.medicine_id.name,
                "quantity": line.quantity,
                "price_unit": line.medicine_id.price,
            }))
        invoice = self.env["account.move"].create({
            "partner_id": partner.id,
            "move_type": "out_invoice",
            "invoice_line_ids": invoice_lines,
        })
        self.invoice_id = invoice.id

    def view_invoice(self):
        self.ensure_one()
        return self.invoice_id.get_formview_action()
