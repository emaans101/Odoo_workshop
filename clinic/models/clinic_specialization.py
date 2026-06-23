from odoo import models, fields


class ClinicSpecialization(models.Model):
    _name = "clinic.specialization"
    _description = "Medical Specialization"

    # Store the docter name, and find all docters who specilise in the given field
    name = fields.Char(required=True)
    doctor_ids = fields.One2many("clinic.doctor", "specialization_id")
