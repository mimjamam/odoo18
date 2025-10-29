from email.policy import default

from odoo import models, fields

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string="Gender")

    address= fields.Char(string="Address")

    ref=fields.Char(string="Reference")

    active=fields.Boolean(string="Active",default=True)