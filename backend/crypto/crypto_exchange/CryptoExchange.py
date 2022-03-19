import base64
import hashlib
import hmac
import json
import time


class CryptoExchange:
    def __init__(self, creds):
        self.creds = creds
        self.method = 'POST'
        self.request_path = ''
        self.headers = {
            'CB-ACCESS-KEY': self.creds['api_key'],
            'CB-ACCESS-SIGN': "",
            'CB-ACCESS-TIMESTAMP': time.gmtime(),
            'CB-ACCESS-PASSPHRASE': self.creds['passphrase']
        }
        self.params = {

        }
        self.body = {

        }
        # TODO: Move to production
        self.BASE_URL = 'https://api-public.sandbox.exchange.coinbase.com'

    def sign_transaction(self):
        message = str(self.headers['CB-ACCESS-TIMESTAMP'])+self.method+self.request_path+json.dumps(self.body)
        key = base64.b64decode(self.creds['secret'])
        h = hmac.new(key, message, hashlib.sha256)
        self.headers['CB-ACCESS-SIGN'] = h.hexdigest()
        print(self.headers)

    def create_transaction(self):
        print("Test")