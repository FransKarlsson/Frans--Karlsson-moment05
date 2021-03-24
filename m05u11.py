pengar=10000
ränta=1.03
with open('ulfKonto.txt', 'w') as uk:
    for i in range(1,16):
        uk.write(f'\nÅr: {i} | {pengar}kr |')

with open('ulfKonto.txt', 'r') as uk:
    print(uk.read())