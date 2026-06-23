from odoo import models, fields


class ClinicPatient(models.Model):
    _inherit = "clinic.patient"

    partner_id = fields.Many2one("res.partner", string="Billing Contact", copy=False)

    def _ensure_billing_partner(self):
        """Return the patient's billing partner, creating one on the fly."""
        self.ensure_one()
        if not self.partner_id:
            self.partner_id = self.env['res.partner'].create({
                'name': self.name,
                'phone': self.phone,
                'email': self.email,
            })
        return self.partner_id
