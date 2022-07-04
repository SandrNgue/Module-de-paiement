# .*. coding: utf-8 .*.

{
    'name': "MTN Money",
    'summary': "Paiement via momo",
    'description': "Gestion de paiement en ligne",
    'author': "Sandra",
    'website': "",
    'category': "Uncategorized",
    'version': "1.0",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv', 
        'views/mtnclient.xml',  
        'views/apimtn.xml',
    ],
    'demo': [],
    'installable' : True,
    'application' : True,
    'images' : 'icon.png', 
    
}