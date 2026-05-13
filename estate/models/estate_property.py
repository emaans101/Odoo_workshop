from odoo import api, fields, models
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Properties"

    name = fields.Char(required = True)
    location = fields.Char()
    living_area = fields.Integer()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    total_area = fields.Integer(compute = "_compute_total_area", store =True)
    property_type_id = fields.Many2one("estate.property.type", string = "Property Type")
    buyer_id = fields.Many2one("res.partner", string = "Buyer")
    salesperson_id = fields.Many2one("res.users", string = "Real Estate Agent", default=lambda self: self.env.user)
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    best_price = fields.Float(compute="_compute_best_price", string = "Best Offer")
    state = fields.Selection(selection=[('new', 'New'), ('offer_received', 'Offer Received'), 
                                        ('offer_accepted', 'Offer Accepted'),
                                        ('sold', 'Sold'), ('cancelled', 'Cancelled')], default='new')
    tag_ids = fields.Many2many("estate.property.tag")

    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area
    
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped("price"))
            else:
                record.best_price = 0.0
    

    def sell_property(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError("Cancelled properties cannot be sold!")
            else:
                record.state = "sold"

    def cancel_property(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold properties cannot be cancelled!")
            else:
                record.state = "cancelled"
