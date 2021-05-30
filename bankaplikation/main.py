from funktioner import *

readFile()
transaktioner.append(1000)

options = '''Välkommen till Franse Bank!

    Vad vill du göra?

    1, visa ditt saldo
    2, sätta in pengar
    3, ta ut pengar
    4, visa dina transaktioner
    0, avsluta aplikationen
    Vad vill du göra?
    '''

while True:
    
    

    command = checkInt(options, 'Felaktig inmatning')
    
    if command == 0:
        break

    elif command == 1:

        print(f'\nDu har {balance()} kr på ditt konto.')

    elif command == 2:
        insättning = checkInt('Hur mycket vill du sätta in?', 'Felaktig inmatning.')
        if insättning > 0:
            addTransaction(insättning)
        else:
            print('\nDu kan inte sätta in en negativ summa pengar.')

    elif command == 3:
        uttag = checkInt('Hur mycket vill du ta ut?', 'Felaktig inmatning')
        if uttag >= 0 and uttag <= balance():
            addTransaction(-uttag)
        else:
            print('\nDu kan inte ta ut så mycket pengar')



    elif command == 4:
        print_transactions()







    else:
        print('felaktigt kommando')
    
