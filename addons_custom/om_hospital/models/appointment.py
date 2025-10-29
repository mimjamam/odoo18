from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Appointment", default="New", tracking=True)
    patient_id = fields.Many2one(
        comodel_name="hospital.patient",
        string="Patient",
        required=True,
        ondelete="cascade",
        tracking=True,
    )
    appointment_date = fields.Datetime(string="Appointment Date", required=True, tracking=True)
    doctor_name = fields.Char(string="Doctor")
    notes = fields.Text(string="Notes")
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("confirm", "Confirmed"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        string="Status",
        default="draft",
        tracking=True,
    )

    @api.model
    def create(self, vals):
        # Assign a simple readable name if not provided
        if not vals.get("name") and vals.get("appointment_date"):
            vals["name"] = f"Appt {vals['appointment_date']}"
        return super().create(vals)

    def action_confirm(self):
        for record in self:
            record.state = "confirm"

    def action_done(self):
        for record in self:
            record.state = "done"

    def action_cancel(self):
        for record in self:
            record.state = "cancel"

    def action_reset_to_draft(self):
        for record in self:
            record.state = "draft"

 


