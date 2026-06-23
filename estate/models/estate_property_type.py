from odoo import api, models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "property types"

    name = fields.Char() #villa, apartment, studio, penthouse etc
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Integer(compute="_compute_offer_count")

    _unique_type_name = models.Constraint("UNIQUE(name)", "A property type must be unique")

    property_ids = fields.One2many("estate.property", "property_type_id")
    
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in  self:
            record.offer_count = len(record.offer_ids)
            