from odoo import models, fields, api


class ClinicDoctor(models.Model):
    _name = "clinic.doctor"
    _description = "Doctor"

    name = fields.Char(required=True)
    phone = fields.Char()
    email = fields.Char()
    # Docters Specilization they belong to
    specialization_id = fields.Many2one("clinic.specialization",string="Specialization")
    user_id = fields.Many2one("res.users",string="Related User") # Provsing docter acess rights to log in
    # One docetr can have many appointments
    appointment_ids = fields.One2many("clinic.appointment","doctor_id")
    # Useful fun features
    consultation_fee = fields.Float(string="Consultation Fee")
    years_of_experience = fields.Integer(string="Years of Experience")

