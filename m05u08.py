poäng = []

with open('provpoäng.txt') as f:
  f=f.read()
  f=f.split("\n")
  f.sort()
  print(f"Sorterat: {f}")
  print(f"Längd: {len(f)}")
  print(f"Medelvärde: {sum(f)/len(f)}")



