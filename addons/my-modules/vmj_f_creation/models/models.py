# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class vmj_f_creation(models.Model):
#     _name = 'vmj_f_creation.vmj_f_creation'
#     _description = 'vmj_f_creation.vmj_f_creation'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields

class Alumni_Form_Record(models.Model):
	_name="res.partner"
	_inherit='res.partner'
	exam=fields.Selection([('icse','ICSE'),('isc', 'ISC')], string="Examination")
	yop=fields.Integer(string="Year Of Passing ICSE/ ISC")
	my_teachers=fields.Char(string="My Teachers")
	qual=fields.Many2one('res.qual', string="Qualification/ Profession Category")
	hqh=fields.Char(string="Highest Qualification Held")
	som=fields.Char(string="Specialization or Major")
	ysk=fields.Char(string="Your Special Skill(In any area of interest)")
	clg=fields.Char(string="Institute/ College/ University")
	ped=fields.Many2one('res.ped', string="Present Employment Status")
	about=fields.Char(string="About Me")
