import requests


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

    def gen_qr_code(self, coin_type: str, address: str, amount: float, message: str):
        self.params['chl'] = f'{coin_type}:{address}?amount={amount:10.10f}&message={message}'
        print(self.params)
        r = requests.get(self.BASE_URL, self.params)
        if r.status_code is 200:
            return r.content
        else:
            raise Exception(r)

