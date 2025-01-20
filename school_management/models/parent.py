from odoo import models, fields, api, _


class Parent(models.Model):
    _name = 'school_management.parent'
    _description = 'Parent'
    _inherit = ['base.person', 'mail.thread', 'mail.activity.mixin']
    _rec_names_search = ['name', 'nick_name']

    occupation = fields.Selection([('Service', 'Service'), ('Business', 'Business'), ('Housewife', 'Housewife'),
                                   ('Other', 'Other')], string='Date of Birth', default_export_compatible=True)
    annual_income = fields.Float()
    child_ids = fields.One2many('school_management.student', 'parent_id', string='Children')
    nick_name = fields.Char()
    parent_id_seq = fields.Char(
        string="Order Reference",
        required=True, copy=False, readonly=True,
        index='trigram',
        default=lambda self: _('New'))
    res_partner_id = fields.Many2one('res.partner', string='Partner')

    @api.model
    def create(self, vals):
        if vals.get('parent_id_seq', _("New")) == _("New"):
            vals['parent_id_seq'] = self.env['ir.sequence'].next_by_code(
                'parent.id.sequence') or _("New")
        return super(Parent, self).create(vals)

    def url_action(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'contactus',
            'target': 'new',
        }

    def cron_birthday_alert(self):
        today = fields.Date.today()
        for record in self.search([]):
            if record.date_of_birth and record.date_of_birth.strftime('%m-%d') == today.strftime('%m-%d'):
                record.message_post(body='Happy Birthday!', subject='Birthday Alert')