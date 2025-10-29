from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hotel Booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'check_in desc'

    name = fields.Char(string='Booking Reference', required=True, copy=False, readonly=True, default='New')
    guest_id = fields.Many2one('hotel.guest', string='Guest', required=True, tracking=True)
    room_id = fields.Many2one('hotel.room', string='Room', required=True, tracking=True)
    check_in = fields.Date(string='Check In', required=True, tracking=True)
    check_out = fields.Date(string='Check Out', required=True, tracking=True)
    num_guests = fields.Integer(string='Number of Guests', default=1)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)
    total_nights = fields.Integer(string='Total Nights', compute='_compute_total_nights', store=True)
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    notes = fields.Text(string='Notes')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('hotel.booking') or 'New'
        return super(HotelBooking, self).create(vals_list)

    @api.depends('check_in', 'check_out')
    def _compute_total_nights(self):
        for booking in self:
            if booking.check_in and booking.check_out:
                delta = booking.check_out - booking.check_in
                booking.total_nights = delta.days
            else:
                booking.total_nights = 0

    @api.depends('total_nights', 'room_id.price_per_night')
    def _compute_total_amount(self):
        for booking in self:
            booking.total_amount = booking.total_nights * booking.room_id.price_per_night

    @api.constrains('check_in', 'check_out')
    def _check_dates(self):
        for booking in self:
            if booking.check_out <= booking.check_in:
                raise ValidationError('Check-out date must be after check-in date!')

    def action_confirm(self):
        self.write({'state': 'confirmed'})
        self.room_id.write({'status': 'occupied'})

    def action_check_in(self):
        self.write({'state': 'checked_in'})

    def action_check_out(self):
        self.write({'state': 'checked_out'})
        self.room_id.write({'status': 'available'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})
        if self.room_id.status == 'occupied':
            self.room_id.write({'status': 'available'})
