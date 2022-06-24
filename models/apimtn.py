# .*. coding: utf-8 .*.

from tokenize import String
from odoo import models, fields

class apimtn(models.Model):
    _name = "apimtn"
    _description = "paiement via momo"
    number = fields.Char('Entrer à nouveau votre numéro de téléphone:')
    image = fields.Binary('Image')

  