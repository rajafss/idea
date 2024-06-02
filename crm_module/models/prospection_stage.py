from odoo import models, fields, api
class ProspectionStage(models.Model):
    _name='prospection.stage'
    _description = 'Pospection Stage'
    _order = 'id asc'


    name = fields.Char(string="Prospection stage")

