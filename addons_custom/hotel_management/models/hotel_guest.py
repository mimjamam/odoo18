from odoo import models, fields


class HotelGuest(models.Model):
    _name = 'hotel.guest'
    _description = 'Hotel Guest'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Guest Name', required=True, tracking=True)
    email = fields.Char(string='Email', tracking=True)
    phone = fields.Char(string='Phone', required=True, tracking=True)
    address = fields.Text(string='Address')
    id_number = fields.Char(string='ID Number', tracking=True)
    booking_ids = fields.One2many('hotel.booking', 'guest_id', string='Bookings')
    booking_count = fields.Integer(string='Total Bookings', compute='_compute_booking_count')
    active = fields.Boolean(default=True)

    def _compute_booking_count(self):
        for guest in self:
            guest.booking_count = len(guest.booking_ids)
