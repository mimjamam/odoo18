from odoo import models, fields, api


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Room Number', required=True, tracking=True)
    room_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        ('deluxe', 'Deluxe'),
    ], string='Room Type', required=True, tracking=True)
    floor = fields.Integer(string='Floor', tracking=True)
    capacity = fields.Integer(string='Capacity', default=1)
    price_per_night = fields.Float(string='Price per Night', required=True, tracking=True)
    status = fields.Selection([
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Maintenance'),
    ], string='Status', default='available', tracking=True)
    description = fields.Text(string='Description')
    amenities = fields.Text(string='Amenities')
    booking_ids = fields.One2many('hotel.booking', 'room_id', string='Bookings')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('room_number_unique', 'unique(name)', 'Room number must be unique!')
    ]
