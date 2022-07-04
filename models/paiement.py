import base64
import http.client, urllib.request, urllib.parse, urllib.error, uuid, json, requests


reference_id = str(uuid.uuid4())
print(reference_id)

headers = {
    # Request headers
    'X-Reference-Id': reference_id,
    
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '625fb6816c354020a719e6e4a60957d7',
    'Ocp-Apim-Subscription-Key2': '625fb6816c354020a719e6e4a60957d7'

}
params = urllib.parse.urlencode({
})
body = json.dumps({
  "providerCallbackHost": 'sandbox.momodeveloper.mtn.com' })
try:
    conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
    conn.request("POST", "/v1_0/apiuser/reference_id/apikey?%s" % params, "{body}", headers)
    # conn.request("POST", "/v1_0/apiuser/<put-your-reference-id-here>/apikey?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

url = 'https://sandbox.momodeveloper.mtn.com/v1_0/apiuser'
body = {"providerCallbackHost": "string"}
r = requests.post(url, data=json.dumps(body), headers=headers)
print(r)
if r.status_code== 201:
            print("Creation de User API")
            url = f'https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/{reference_id}/apikey'
            body = {"providerCallbackHost": "string"}
            r = requests.post(url, data=json.dumps(body), headers=headers)
            print(r)
            print(r.content)
            user_key_tojson = r.json()
            apikey = user_key_tojson['apiKey']
            print('API crée avec success:', apikey)
            
#basic
api_user_and_key  = reference_id+':'+apikey
encoded = base64.b64encode(api_user_and_key.encode()).decode()
print('basic encode:', encoded)
url = "https://sandbox.momodeveloper.mtn.com/collection/token/"
r = requests.post(url, headers=headers, auth=(reference_id, apikey))            
if r.status_code== 200:
                json_content = r.json()
                access_token = json_content['access_token']
                token_type = json_content['token_type']
                expires_in = json_content['expires_in']
                print('access_token :', access_token)
                print('token_type :', token_type)
                print('expires_in :', expires_in)

#request
headers = {
    # Request headers
    'Authorization': 'Bearer %s' % access_token,
    'X-Reference-Id': reference_id,
    'X-Target-Environment': 'sandbox',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '625fb6816c354020a719e6e4a60957d7',
}
params = urllib.parse.urlencode({
})

body = json.dumps({
  "amount": "1",
  "currency": "EUR",
  "externalId": "12345",
  "payer": {
    "partyIdType": "MSISDN",
    "partyId": "237653865107"
  },
  "payerMessage": "test message",
  "payeeNote": "test note"
})

try:
    conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
    conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


#retrait

params = urllib.parse.urlencode({
})

body= ({
  "payeeNote": "azerty",
  "externalId": "1245",
  "amount": "",
  "currency": "EUR",
  "payer": {
    "partyIdType": "MSISDN",
    "partyId": ""
  },
  "payerMessage": "MERCI"
})

try:
    conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
    conn.request("POST", "/collection/v1_0/requesttowithdraw?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))