from config import *

def test_file_exists():
    try:
        with open(filename, 'x'):
            print('Filen skapades')
    
        with open(filename, 'a') as f:
            f.write('{}\n'.format(1000))
    except:
        return

def readFile():
    test_file_exists()
    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                transaktioner.append(int(rad))

def addTransaction(transaction):
    transaktioner.append(transaction)
    with open(filename, 'a') as f:
        f.write('{}\n'.format(transaction))



def balance():
    balance = 0
    for t in transaktioner:
        balance += t
    return balance

def checkInt(output, errorMsg):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(errorMsg)
    return value

def print_transactions():
    line = 0
    sum = 0
    head =  ('\nAlla transaktioner:'
    '\n{:>3} {:>12} {:>12}'
    '\n--------------------------------').format('Nr', 'Händelse', 'Saldo')
        
    print(head)
    for t in transaktioner:
        line += 1
        sum += t
        print('{:>2}. {:>9} kr {:>9} kr'.format(line, t, sum))
