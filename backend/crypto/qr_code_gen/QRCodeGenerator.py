import requests
import os


class QRCodeGenerator:
    def __init__(self):
        self.params = {
            "cht": "qr",
            "chl": "",
            "chs": "180x180",
            "choe": "UTF-8",
            "chld": "L|2"
        }

        self.BASE_URL = "https://chart.googleapis.com/chart"

    def gen_qr_code(self, coin_type: str, address: str, amount: float, id: int):
        amount = round(amount, 8)
        # Tag bit, 1 for crypto-square transactions
        id += 10000000
        amount += id/10000000000000000
        print(amount)
        self.params['chl'] = f'{coin_type}:{address}?amount={amount:2.16f}'
        print(self.params)
        r = requests.get(self.BASE_URL, self.params)
        if r.status_code == 200:
            with open("static/QR.png", "wb") as f:
                f.write(r.content)
        else:
            raise Exception(r)

