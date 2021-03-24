# Öppnar provpoäng och gör varge rad till en del av en lista
with open('provpoäng.txt') as f:
  f=f.read()
f=f.split("\n")

# Gör varge elev till ett dictionary med poäng och namn.
elever=[]
for i in f:
    elever.append({'namn': i[0:i.find("|")], "poäng": int(i[i.find("|")+1:]) })

#sorterar eleverna efter poäng
eleverSorted=sorted(elever, key=lambda i: i['poäng'])

#Printar alla poäng lägst tilll högst
for i in eleverSorted:
  print(i['namn'],i['poäng'])

# printar ut medelpoängen av alla elever
total = 0
for i in elever:
  total+=i['poäng']
print('\n Medelvärdet för provpoängen:')
print(total/len(elever))

# Printar det bästa respektive sämsta resultatet
print('eleven med högst poäng var:,',end=' ')
print({eleverSorted[-1]['namn']},end=' ')

print('eleven med lägst poäng var:,',end=' ')
print({eleverSorted[0]['namn']},end=' ')