from odoo import models, fields


class ClinicAppointment(models.Model):
    _name = "clinic.appointment"
    _description = "Appointment"

    patient_id = fields.Many2one(
        "clinic.patient",
        string="Patient",
        required=True
    )

    doctor_id = fields.Many2one(
        "clinic.doctor",
        string="Doctor",
        required=True
    )

    date_start  = fields.Datetime(
        string="Appointment Date",
        required=True
    )

    reason = fields.Text()

    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='scheduled')