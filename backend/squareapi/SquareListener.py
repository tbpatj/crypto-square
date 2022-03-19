import time
import threading
from square.client import Client
from squareapi import get_open_orders_at_location

# config
SQUARE_API_POLL_TIME_SEC = 1

#login stuff
SQUARE_APP_ID = 'sandbox-sq0idb-kxIfsS4_R9UYfFIwVznQIg'
#sandbox
#SQUARE_ACCESS_TOKEN = 'EAAAEE23Tjnaem9aZBCJ4eHvk7cqJh7FnjcxG5HC-_plFd7i_Am0tiPm1eUTT2Mr'
#production
SQUARE_ACCESS_TOKEN = 'EAAAEGdGIcJvY4YLQB2oqK_1btrzqq4Y8am-050ljSr-a7vhx77sGRzQLKaaIijD'
CRYPTOSQUARE_CUSTOMER_ID = 'H2K6GCD9CN6DZ04NZM063G0S40'

client = Client(
    square_version='2022-03-16',
    access_token=SQUARE_ACCESS_TOKEN,
    #environment='sandbox'
)

# placeholders for backend
list_of_merchants = [
    {
        'merchant_id': 'S9C80RF9GPRD8',
        'locations': [
            'S9C80RF9GPRD8'
        ]
    }
]

ids_of_known_open_orders = []

class SquareListener():
    def __init__(self):
        self.listener_thread = threading.Thread(target=self.listener_main)
        self.listener_thread.start()
        print('square api listener created.')
    
    def listener_main(self):
        while True:
            # for all merchants, check for recent invoices to CryptoSquare
            for merchant in list_of_merchants:
                for location in merchant['locations']:
                    open_orders = get_open_orders_at_location(location)
                    for order in open_orders:
                        #is already logged?
                        if order['id'] not in ids_of_known_open_orders:
                            print('new order <%s> found! would trigger new xaction!' % order['id'])
                            # do something with the xaction data
                            ids_of_known_open_orders.append(order['id'])
                        else:
                            #found existing order
                            pass
            time.sleep(SQUARE_API_POLL_TIME_SEC)

square_listener = SquareListener()
time.sleep(10)
