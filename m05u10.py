
with open('utskrift.txt', 'w') as fw: # Öppnar utskrift.txt med skrivläge i variabeln fw.
  fw.write('''1 2 3 
4 5 6
7 8 9
''') # Skrier talen 1 - 9 i en 3*3 kvadrat i dokumentet.
  fw.write('\nHär var det rutigt!') # Skriver Här var det rutigt i dokumentet på en ny rad.
with open('utskrift.txt', 'r') as fr: # Öppnar dokumentet i läsläge i variabeln fw.
  print(fr.read()) # Printar ut dokumentets innehåll.