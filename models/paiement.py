from lib2to3.pgen2 import token
from os import access
from re import sub
from wsgiref import headers
from odoo import models, fields
import requests
import json
import uuid
import random


class Paiement(models.Model):
    
    _name = 'paiement'
    _description = 'generation token'
    token = fields.Char('Votre token')
    state = fields.Selection([('en_cours', 'En cours'), ('activer', 'Activer'), ('desactiver', 'Désactiver')], string='Status', default='en_cours', tracking=True)
    
    
    # @api.depends('token', 'paiement', 'state')
    # def execute(self):
    #    if self.state == 'activer':
    #        self.token = self.paiement
    #    else:
    #        self.state = 'desactiver'
           
          
def paiement(self):
        #definition des parametres

        subscription_key_user_create = '625fb6816c354020a719e6e4a60957d7'
        subscription_key_trans_create = '4d9669aa-54f4-44ae-acae-be77803bc687'
        reference = str(uuid.uuid4())
        url = 'https://sandbox.momodeveloper.mtn.com/v1_0/apiuser'
        body = {"providerCallbackHost": "string"}
        headers = {'X-Reference-Id': reference, 'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': subscription_key_user_create}

        #creation d'un user

        r = requests.post(url, data=json.dumps(body), headers=headers)
        print(r)

        #creation de l'api key

        if r.status_code== 201:
            print("Creation de User API")
            url = f'https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/{reference}/apikey'
            body = {"providerCallbackHost": "string"}
            headers = {'Ocp-Apim-Subscription-Key': subscription_key_user_create}
            r = requests.post(url, data=json.dumps(body), headers=headers)
            print(r)
            print(r.content)
            user_key_tojson = r.json()
            apikey = user_key_tojson['apiKey']
            print('API crée avec success:', apikey)
            
            print('Done!')
            
            #token
            url = "https://sandbox.momodeveloper.mtn.com/collection/token/"
            headers = {'Ocp-Apim-Subscription-Key': subscription_key_trans_create}
            r = requests.post(url, headers=headers, auth=(reference, apikey))
            
            if r.status_code== 200:
                json_content = r.json()
                access_token = json_content['access_token']
                token_type = json_content['token_type']
                expires_in = json_content['expires_in']
                print('access_token :', access_token)
                print('token_type :', token_type)
                print('expires_in :', expires_in)
                
                montant = 2000
                devise = 'EUR'
                id = '123456'
                payor_phone = '237698006133'
                payer_message = "Paiement numero 12345"
                payee_message = "Reglement OrderID: 1234"        
                body = {
                    'amount': montant,
                    'currency': devise,
                    'externalId': id,
                    'payer': {'partyIdType': 'MSISDN', 'partyId': payor_phone},
                    'payerMessage': payer_message,
                    'payeeNote': payee_message
                }
                headers = {
                    'Authorization': 'Bearer '+ access_token,
                    'X-Reference-Id': reference,
                    'X-Target-Environment': 'sandbox',
                    'Content-Type': 'application/json',
                    'Ocp-Apim-Subscription-Key': subscription_key_trans_create,
                }    
                url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"  
                    
                r = requests.post(url, data=json.dumps(body).encode("ascii"), headers=headers)
                print(r)
                print("la transaction est correcte")