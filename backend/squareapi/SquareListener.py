import time
import threading
from square.client import Client
from squareapi.squareapi import get_open_orders_at_location
import main.views;
from main.models import Merchant

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

ids_of_known_open_orders = [ 'inv:0-ChDg2xbRaNgYaamJ-qRRjxbPEKwL', 'inv:0-ChDct2EiE1urmfhs4wxMRsZVEKwL', 'inv:0-ChB6vY8MCUT89cEopp2YtZxaEKwL', 'inv:0-ChAJk5Sep86-05Ev7618ZUPmEKwL','inv:0-ChD19iDJa_9sRrahQpzL-QtfEKwL', 'inv:0-ChBLmkw1KXm6LpfFtA6iNjCIEKwL', 'inv:0-ChDWgs0njhFm8hzO22-v7r6PEKwL']

class SquareListener():
    def __init__(self):
        #self.init_list_of_merchants()
        #self.get_init_transactions()
        #time.sleep(1)
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
                            print('new order <%s> found!');
                            # do something with the xaction data
                            order_amt = order['payment_requests'][0]['computed_amount_money']['amount'] # TODO: check and make sure invoices arent just the first indice lol
                            invoice_id = order['id']
                            created_date = order['created_at']
                            location_id = order['location_id']
                            merchant_id = merchant['merchant_id']
                            print('invoice amt: $%d, id: %s, created: %s, location id: %s, merchant id: %s' % (order_amt / 100, invoice_id, created_date, location_id, merchant_id))
                            
                            # call view object so they can link this stuff up and make a transaction
                            main.views.new_order(invoice_id=invoice_id, order_amount_fiat=order_amt, sq_merchant_id=merchant_id)

                            # append to fake db
                            ids_of_known_open_orders.append(order['id'])
                        else:
                            #found existing order
                            pass
            time.sleep(SQUARE_API_POLL_TIME_SEC)
    
    def init_list_of_merchants(self):
        for merchant in Merchant.objects.all():
            ids_of_known_open_orders.append(merchant.sq_merchant_id)

    def get_init_transactions(self):
        # for all merchants, check for recent invoices to CryptoSquare
        for merchant in list_of_merchants:
            for location in merchant['locations']:
                open_orders = get_open_orders_at_location(location)
                for order in open_orders:
                    #is already logged?
                    if order['id'] not in ids_of_known_open_orders:
                        print('past order <%s> found!');
                        ids_of_known_open_orders.append(order['id'])
                    else:
                        #found existing order
                        pass