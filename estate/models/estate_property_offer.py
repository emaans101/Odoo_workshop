from odoo import api, models, fields
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offers"

    price = fields.Float(required=True)
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')])

    def accept_offer(self):
        for record in self:
            if record.property_id.state == "offer_accepted":
                raise UserError("This property already has an offer accepted!")
            else:
                record.status = "accepted"
                record.property_id.state = "offer_accepted"
                record.property_id.buyer_id = record.partner_id.id
                record.property_id.selling_price = record.price

    def refuse_offer(self):
        for record in self:
            if record.status == 'accepted':
                raise UserError('Accepted offers cannot be refused')
            else:
                record.status = "refused"

    