# .*. coding: utf-8 .*.
from odoo.exceptions import ValidationError
from odoo import models, api, fields, _

class mtnclient(models.Model):
    _name = "mtnclient"
    _description = "paiement via momo"
    code_compte = fields.Char(string='Entrer le code de votre compte:', required=True, tracking=True)
    phone_number = fields.Char('Entrer votre numéro de téléphone:')


    @api.constrains('code_compte')     
    def _check_code_duplicate(self):
        code_rec = self.env['mtnclient'].search(
            [('code_compte', '=', self.code_compte), ('id', '!=', self.id)])
        if code_rec:
            raise ValidationError(_('ERROR DUPLICATE: Code Already Exixt!!!'))
        else:
            pass