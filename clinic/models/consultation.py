from odoo import api, models, fields


class ClinicConsultation(models.Model):
    _name = "clinic.consultation"
    _description = "Consultation"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "date desc"

    name = fields.Char(compute="_compute_name", store=True)
    appointment_id = fields.Many2one("clinic.appointment", readonly=True)
    patient_id = fields.Many2one("clinic.patient", string="Patient", required=True)
    doctor_id = fields.Many2one("clinic.doctor", string="Doctor", required=True)
    date = fields.Datetime(default=fields.Datetime.now)
    symptoms = fields.Text()
    diagnosis = fields.Text()
    notes = fields.Text()
    temperature = fields.Float(string="Temperature (°C)")
    blood_pressure = fields.Char(string="Blood Pressure")
    weight = fields.Float(string="Weight (kg)")
    prescription_line_ids = fields.One2many("clinic.prescription.line", "consultation_id")
    state = fields.Selection(
        selection=[('draft', 'Draft'), ('done', 'Done')],
        default='draft', required=True, tracking=True,
    )

    @api.depends("patient_id", "date")
    def _compute_name(self):
        for record in self:
            record.name = "Consultation - %s" % (record.patient_id.name or "New")

    def action_done(self):
        for record in self:
            record._dispense_prescription()
            record.state = 'done'
            if record.appointment_id:
                record.appointment_id.state = 'done'

    def _dispense_prescription(self):
        """Dispense prescribed medicines by decrementing stock.

        Overridden by the ``clinic_stock`` bridge to post real Odoo Inventory
        moves when a medicine is linked to a product.
        """
        self.ensure_one()
        for line in self.prescription_line_ids:
            if line.medicine_id:
                line.medicine_id.qty_available -= line.quantity


class ClinicPrescriptionLine(models.Model):
    _name = "clinic.prescription.line"
    _description = "Prescription Line"

    consultation_id = fields.Many2one("clinic.consultation", required=True, ondelete="cascade")
    medicine_id = fields.Many2one("clinic.medicine", string="Medicine", required=True)
    dosage = fields.Char(string="Dosage / Instructions")
    quantity = fields.Float(default=1.0)
