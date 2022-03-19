import json
import threading
import time

import requests

from main.update_transactions import pending_transaction, completed_transaction, failed_transaction


class WalletListener:
    def __init__(self, address: str):
        self.address = address
        self.all_transactions = []
        self.pending_transactions = []
        self.listener_active = False

        # old api key: ZI345ST1IVEWCH5HUE95IAFKQMH24XXGFM
        print(self.address)
        self.params = {
            "module": "account",
            "action": "txlist",
            "address": self.address,
            "startblock": 0,
            "endblock": 99999999,
            "offset": 10,
            "page": 1,
            "sort": "desc",
            "apikey": "juab3erfgxhgnpji3tdjaqdzpve5b8axmd"
        }
        # TODO: Switch to prod
        self.BASE_URL = "https://api.etherscan.io/api"

    def run(self):
        print("Start thread.")
        x = threading.Thread(target=self.task)
        x.start()
        return x

    def task(self):
        self.listener_active = True

        # Set current transactions
        r = requests.get(self.BASE_URL, params=self.params, headers={"User-Agent": ""})
        print(r.content)
        self.all_transactions = [t['hash'] for t in json.loads(r.content)['result']]
        # 100000 per day -> 1.69 calls per second
        # or 5 calls per second
        while self.listener_active:
            # Every 1/4 of a second check for first pending transaction
            # TODO: WHEN YOU PUSH TO PROD, RUN IT LIKE MAD
            time.sleep(1)
            print('WL active.')
            r = requests.get(self.BASE_URL, params=self.params, headers={"User-Agent": ""})
            r = json.loads(r.content)['result']
            new_pending = [transaction for transaction in r if transaction['hash'] not in self.all_transactions]
            for transaction in new_pending:
                if transaction['hash'] in self.pending_transactions and transaction['txreceipt_status'] == '1':
                    self.all_transactions.append(transaction['hash'])
                    self.pending_transactions.remove(transaction['hash'])
                    self.transaction_completed(transaction)
                elif transaction['hash'] not in self.pending_transactions:
                    self.pending_transactions.append(transaction['hash'])
                    self.transaction_pending(transaction)
                else:
                    print("Transaction pending.")

    def transaction_pending(self, transaction):
        print("Transaction " + transaction['hash'] + " is pending.")
        pending_transaction(transaction)

    def transaction_completed(self, transaction):
        print("Transaction " + transaction['hash'] + " is is complete.")
        completed_transaction(transaction)
