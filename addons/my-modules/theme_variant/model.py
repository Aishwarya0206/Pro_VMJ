from odoo import models, fields

class AlumniRecord(models.Model)
	_name="alumni.alumni"
	name=fields.Char(string="Name", required="True")
	alumni_dob=fields.Date(string="Date Of Birth", required="True")
	exam=fields.Selection([('icse','ICSE'),('isc', 'ISC')])
	yop=fields.Integer(string="Year Of Passing ICSE/ ISC")
	my_teachers=fields.Char(string="My Teachers")
	city=fields.Char(string="City", required="True")
	state=fiels.Char(string="State", required="True")
	country=fields.Char(string="Country", required="True")
	mob_no=fields.Integer(string="Mobile No.")
	email=fields.Char(string="Email")
	qual=fields.Many2one('res.qual', string="Qualification/ Profession Category")
	hqh=fields.Char(string="Highest Qualification Held", required="True")
	som=fields.Char(String="Specialization/ Major", required="True")
	ysk=fields.Char(string="Your Special Skill(In any area of interest)"
	clge=field.Char(string="Institute/ College/ University", required="True")
	ped=fields.Many2one('res.ped', String="Present Employment Status")
	about=fields.Char(string="About Me")
	photo=fields.Binary(string="Upload Photo")
