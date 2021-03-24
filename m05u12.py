with open('u12.txt', 'w') as f:
    tal = []
    högst=0
    lägst=0
    summa=0
    while True:
        x = int(input('Skriv in ett tal. (0 avslutar programmet)'))
        lägst = x
        if x == 0:
            break
        else:
            tal.append(x)
            summa+=x
        
        for i in tal:
            if högst < i:
                högst = i
            
            if lägst > i:
                lägst = i
        f.write(f'\nHögsta talet:{högst}, Lägsta talet: {lägst}, Summan av talen:{summa}')
    




        