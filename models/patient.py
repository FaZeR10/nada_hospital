from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'all patients details needed'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    ID = fields.Integer(string='Integer Field')
    Gender = fields.Boolean(string='Boolean Field')
    entery_date = fields.Date(string='Date Field')

    #selection_field = fields.Selection(
     #   selection=[('option1', 'Option 1'), ('option2', 'Option 2')],
      #  string='Selection Field',
       # default='option1')