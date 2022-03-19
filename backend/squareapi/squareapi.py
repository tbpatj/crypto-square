from square.client import Client
import time
from datetime import datetime, timedelta

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

def get_merchant_and_main_location_id():
    locations_api = client.locations
    merchant_locations_request = locations_api.list_locations()

    if merchant_locations_request.is_success():
        print("merchant has %d locations" % len(merchant_locations_request.body['locations']))

        # TODO: add ways to connect alternate locations
        main_location_id = merchant_locations_request.body['locations'][0]['id']
        merchant_id = merchant_locations_request.body['locations'][0]['id']

        print("using main location with id of %s" % main_location_id)
        print("merchant id is %s" % merchant_id)
        return main_location_id
    else:
        print('error getting list of merchant locations')
        print(merchant_locations_request.errors)
        return -1

def get_open_orders_at_location(search_location_id):
    open_invoices = []
    
    get_open_invoices_request = client.invoices.list_invoices = client.invoices.search_invoices(
        body = {
            "query": {
                "filter": {
                    "location_ids": [
                        search_location_id
                    ],
                    "customer_ids": [
                        CRYPTOSQUARE_CUSTOMER_ID
                    ]
                }
            }
        }
    )
    
    if get_open_invoices_request.is_success():
        for invoice in get_open_invoices_request.body['invoices']:
            if invoice['status'] == 'UNPAID':
                if datetime.fromisoformat(invoice['created_at'][:-1]) > (datetime.now() + timedelta(minutes=-30)):
                    # we got one! it might have already been detected but this IS valid
                    open_invoices.append(invoice)
                    #print('new order!')
                else:
                    #print('too old')
                    pass
            else:
                #print('paid')
                pass
    else:
        #
        print('error getting open invoices from square!')
        print(get_open_invoices_request.errors)
    
    return open_invoices
    

#start
#print('\n\n\n')
#print('getting location id for client...')
#merchant_location_id = get_merchant_and_main_location_id()

#while True:
#    print('polling for new orders...')
#    get_open_orders_at_location(merchant_location_id)
#    time.sleep(1)