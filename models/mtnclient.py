# .*. coding: utf-8 .*.
from odoo.exceptions import ValidationError
from odoo import models, api, fields, _

class mtnclient(models.Model):
    _name = "mtnclient"
    _description = "paiement via momo"
    phone_number = fields.Char('Entrer votre numéro de téléphone:', required=True, tracking=True)
    amount = fields.Char('Entrer le montant à verser:', required=True, tracking=True)

    def action_get_data(self):
        print("send data")
        temp_id= self.env.ref('/').id
        self.env['phone.template'].browse(temp_id).send_phone(self.id, force_send=True)
    # code_compte = fields.Char(string='Entrer le code de votre compte:', required=True, tracking=True)
    # @api.constrains('code_compte')     
    # def _check_code_duplicate(self):
    #     code_rec = self.env['mtnclient'].search(
    #         [('code_compte', '=', self.code_compte), ('id', '!=', self.id)])
    #     if code_rec:
    #         raise ValidationError(_('ERROR DUPLICATE: Code Already Exixt!!!'))
    #     else:
    #         pass