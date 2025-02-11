import os
import requests
from dotenv import load_dotenv

load_dotenv()

headers = {
    'X-Api-Key': os.environ['lnbits_invoice_key'],
    'Content-type': 'application/json',
}

data = '{"out": false, "amount":1000, "memo":"dalle2bot", "unit":"sat"}'

def getinvoice():
  response = requests.post('https://legend.lnbits.com/api/v1/payments', headers=headers,   data=data)
  return response.json()

def checkinvoice(payment_hash):
  response = requests.get('https://legend.lnbits.com/api/v1/payments/'+payment_hash, headers=headers, data=data)
  result = response.json()
  return result['paid']

#def refund():
#   sth sth lnurlw