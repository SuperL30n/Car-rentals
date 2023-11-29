import requests
from django.conf import settings


url = 'https://api.paystack.co/transaction/initialize'
headers = {'authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}'}



def make_payment(amount:int, email:str):
    _amount = amount*100
    r = requests.post(url,headers=headers, data={'amount':_amount,'email':email})
    response = r.json()
    authorization_url = response['data']['authorization_url']
    refrence = response['data']['reference']
    data = {'reference':refrence, 'auth_url':authorization_url}
    return data


def verify_payment(reference:str):
    url_2 = f'https://api.paystack.co/transaction/verify/{reference}'
    r2 = requests.get(url=url_2,headers=headers)
    resp = r2.json()
    payment_status = resp['data']['status']
    return payment_status

