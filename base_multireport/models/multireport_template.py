# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class MultireportTemplate(models.Model):
    _name = "multireport.template"
    _description = "Multi Report Template"

    name = fields.Char(
        'Name of report template',
        required=True,
        help="Give a unique name for this report template")
    header_mode = fields.Selection(
        [('', 'From style'),
         ('standard', 'Full Odoo Standard'),
         ('logo', 'Only wide logo'),
         ('only_logo', 'Only wide logo / no sep. line'),
         ('line-up', 'Line-up logo / slogan'),
         ('line-up2', 'Line-up logo / slogan / no sep. line'),
         ('line-up3', 'Line-up: logo / company data'),
         ('lin3-up4', 'Line-up: logo / company data / no sep. line'),
         ('no_header', 'No print Header'),
         ],
        'Header Print Mode',
        help="Which content is printed in document header",
    )
    address_mode = fields.Selection(
        [('', 'From style'),
         ('standard', 'Standard Invoice + Shipping'),
         ('only_one', 'Only specific address'),
         ],
        'Address Print Mode',
        help="Which addresses are printed in document header",
    )
    logo_style = fields.Char(
        'Html logo style',
        help='Html style attribute for logo <img> tag.\n'
             'i.e. "max-height: 45px;"'
    )
    payment_term_position = fields.Selection(
        [('', 'From style'),
         ('odoo', 'Odoo'),
         ('auto', 'Auto'),
         ('footer', 'On Footer'),
         ('header', 'On Header'),
         ('none', 'None')
         ],
        'Payment term layout position',
        help='Where Payment term and due dates are printed:\n'
             'may be Auto, None, on Footer, on Header or None\n'
             'If "auto", when due payment is whole in one date,\n'
             'all datas are printed on header otherwise on footer\n'
             'If "Odoo" print only Payment Term notes on Footer',
    )
    footer_mode = fields.Selection(
        [('', 'From style'),
         ('standard', 'Odoo Standard'),
         ('auto', 'Automatic Footer'),
         ('custom', 'Customized Footer'),
         ('no_footer', 'No print Footer'),
         ],
        'Footer Print Mode',
        help='Which content is printed in document footer\n'
             'If "standard", footer is printed as "auto" or "custom"\n'
             'based on company.custom_footer field (Odoo standaed behavior)\n'
             'If "auto", footer is printed with automatic data\n'
             'If "custom", footer is printed from user data written\n',
    )
    code_mode = fields.Selection(
        [('', 'From style'),
         ('noprint', 'No print'),
         ('print', 'Print'),
         ],
        'Print code in document line',
        help='If you choice "print", please set description mode to "nocode"',
    )
    description_mode = fields.Selection(
        [('', 'From style'),
         ('as_is', 'As is'),
         ('line1', 'Only first line'),
         ('nocode', 'No code'),
         ('nocode1', 'No code & Only first line'),
         ],
        'Print description in document line',
        help="Which content is printed in document line",
    )
    order_ref_text = fields.Char(
        'Text with order ref',
        help='Order reference text to print in document body.\n'
            'May be used following macroes:\n'
            '%(client_order_ref)s => Customer reference in order\n'
            '%(order_name)s => Sale order number\n'
            '%(date_order)s => Sale order date.\n'
            'i.e. "Order #: %(order_name)s - Your ref: %(client_order_ref)s"',
        default='Vs. Ordine: %(client_order_ref)s / '\
                'Ns. Ordine: %(order_name)s del %(date_order)s'
    )
    ddt_ref_text = fields.Char(
        'Text with delivery ref',
        help='Delivery reference text to print in document body.\n'
            'May be used following macroes:\n'
            '%(ddt_number)s => Delivery document number.\n'
            '%(date_ddt)s => Delivery document date\n'
            '%(date_done)s => Delivery date\n'
            'i.e. "Ddt #: %(ddt_number)s of %(date_ddt)s"',
        default='DdT %(ddt_number)s - %(date_ddt)s'
    )
    bottom_text = fields.Text(
        'Bottom text',
        help='Text to print in bottom area of document'
    )
    pdf_watermark = fields.Binary('Watermark')
    pdf_watermark_expression = fields.Char(
        'Watermark expression',
        help='An expression yielding the base64 '
             'encoded data to be used as watermark.\n'
             'You have access to variables `env` and `docs`')
    pdf_ending_page = fields.Binary(
        'Ending Page PDF',
        help='If you want the last page of every document printed '
             'to contain some specific content such as Advertisement, '
             'your business terms and Conditions, '
             'upload a PDF with those content here and '
             'it will be appended to every document you print.')
    pdf_ending_page_expression = fields.Char(
        'Ending Page PDF expression',
        help='An expression yielding the base64 '
             'encoded data to be used as Ending Page PDF.\n'
             'You have access to variables `env` and `docs`')
    header_id = fields.Many2one(
        'ir.ui.view', 'Related header',
        required=True,
        domain=[('type', '=', 'qweb'),
                ('inherit_id', '=', False),
                ('name', 'like', 'header')],
        help="Name of header associated to this template")
    footer_id = fields.Many2one(
        'ir.ui.view', 'Related footer',
        required=True,
        domain=[('type', '=', 'qweb'),
                ('inherit_id', '=', False),
                ('name', 'like', 'footer')],
        help="Name of footer associated to this template")
