# Static functions
from main.models import Transaction


def pending_transaction(c_transaction):
    print(c_transaction['value'])
    uid = str(c_transaction['value'])
    uid = uid[len(uid)-10:len(uid)-2]
    print(uid)
    transaction = Transaction.objects.get(crypto_uid=uid)
    transaction.state = 'Transaction pending.'
    transaction.save()
    print(transaction.state)

def completed_transaction(c_transaction):
    print(c_transaction['value'])
    uid = str(c_transaction['value'])
    uid = uid[len(uid)-10:len(uid)-2]
    print(uid)
    transaction = Transaction.objects.get(crypto_uid=uid)
    transaction.state = 'Transaction complete.'
    transaction.save()
    print(transaction.state)

def failed_transaction(c_transaction):
    print("Failed")