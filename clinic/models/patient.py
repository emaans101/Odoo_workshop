from odoo import models, fields, api


class ClinicPatient(models.Model):
    _name = "clinic.patient"
    _description = "Patient"

    name = fields.Char(required=True)
    age = fields.Integer(required=True)
    gender = fields.Selection([('male', 'Male'),('female', 'Female')])
    phone = fields.Char()
    email = fields.Char()
    last_visit_date = fields.Date()
    notes = fields.Text()
    image = fields.Image()
    # Blood group of the patient
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('o+', 'O+')
    ])
    # One patient can have many appointments and consultations
    appointment_ids = fields.One2many("clinic.appointment","patient_id")
    consultation_ids = fields.One2many("clinic.consultation","patient_id")
