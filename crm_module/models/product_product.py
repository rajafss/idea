from odoo import models, fields, api

class ProductproductArgument(models.Model):
    _inherit = 'product.product'


    argument_ids = fields.Many2many("argument.argument" ,string="Argument")

    prospection_stage_id = fields.Many2many('prospection.stage', string="Prospection stage")

    activity_type_id = fields.Many2one(
        'mail.activity.type', string='Activity Type',
    )




class ProductArgument(models.Model):
    _inherit = 'product.template'


    argument_ids = fields.Many2many("argument.argument" ,string="Argument")

    prospection_stage_id = fields.Many2many('prospection.stage', string="Prospection stage")

    description = fields.Text()





