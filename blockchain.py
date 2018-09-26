#Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    """Returns the last value of the current blockchain."""
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain"""
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    return float(input('Your transaction amount please: '))
  
tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=0.9)

tx_amount = get_user_input()
add_value(10.89, get_last_blockchain_value())

print(blockchain)