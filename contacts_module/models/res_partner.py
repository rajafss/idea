from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'


    ###################################################
    ## Method
    ###################################################
    def get_default(self):
        """To count the number of companies saved in contacts we will create a compute field"""
        return self.search_count([('is_industry', '=', True),('is_opposite', '=', False)])

    ###################################################
    ## Business fields
    ###################################################

    factory_ids = fields.One2many('res.partner','factory')

    factory = fields.Many2one('res.partner', string="Factory name")

    category_id = fields.Many2many('res.partner.category', column1='partner_id',
                                   column2='category_id')
    reason_Social = fields.Char()
    legal_status = fields.Many2one('forme.juridique')
    responsible = fields.Char(string="First manager", required=1)
    title = fields.Many2one('res.partner.title')
    sector = fields.Many2one('res.partner.industry' ,string="Sector/Category")
    email_seat = fields.Char()
    email_factory = fields.Char()
    phone_factory = fields.Char(widget='phone')
    phone_seat = fields.Char(widget='phone')
    mobile_seat = fields.Char(widget='phone')
    mobile_factory = fields.Char(widget='phone')
    fax_factory = fields.Char(widget='phone',)
    fax_seat = fields.Char(widget='phone')
    diet = fields.Selection([('exportatrice', 'Totalement exportatrice'),
                               ('non exportatrice ', 'Non Totalement exportatrice')])
    code_tva = fields.Char(string="Code TVA")
    product = fields.Char()
    participant = fields.Char( string='Country of foreign participant')
    date = fields.Char(string=" Production entry date")
    capital = fields.Integer(string="Share capital in DT" )
    job = fields.Integer()
    street_seat = fields.Char()
    street_factory = fields.Char()
    city_factory = fields.Many2one('delegation',
                                domain="[('state_id', '=?', state_factory)]")
    city_seat = fields.Many2one('delegation',
                                      domain="[('state_id', '=?', state_seat)]")
    state_factory = fields.Many2one("res.country.state", ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_seat = fields.Many2one('res.country', ondelete='restrict')
    state_seat = fields.Many2one("res.country.state",ondelete='restrict',
                                     domain="[('country_id', '=?', country_seat)]")
    zip_seat = fields.Char(string="Seat postal code" ,change_default=True)
    zip_factory = fields.Char(string="Factory postal code",change_default=True)
    is_industry = fields.Boolean()
    is_opposite = fields.Boolean(string="Est un vis à vis", required=1)
    product_id = fields.Char(string="Product")
    # compute field recalculate the company nomber
    nb_company = fields.Integer(
        compute='_compute_total',
        default=get_default,  # Using the get_default function as the default value
        reverse=True
    )

    #################################################
    ##Compute Method
    #################################################
    def _compute_total(self):
        """we need this function to calculate the number of company saved"""
        for partner in self:
            partner.nb_company = self.search_count([('is_industry', '=', True),('is_opposite', '=', False)])


