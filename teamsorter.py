import random

allplayers=[]
red=[]
blue=[]

print("Enter the names of the 10 players.")
for i in range(10):
  names=input("Player "+str(i+1)+": ")
  allplayers.append(names)

print("\nPlayers:\n ")
a=1
for item in allplayers:
  print(" "+str(a)+". "+item)
  a+=1

while len(allplayers)>0:
  x=random.choice(allplayers)
  red.append(x)
  allplayers.remove(x)
  y=random.choice(allplayers)
  blue.append(y)
  allplayers.remove(y)
  print("\nTeam Red: ")
  b=1
  for item1 in red:
    print(" "+str(b)+". "+item1)
    b+=1
  print("Team Blue: ")
  c=1
  for item2 in blue:
    print(" "+str(c)+". "+item2)
    c+=1
  print("Players left: ")
  d=1
  for item3 in allplayers:
    print(" "+str(d)+". "+item3)
    d+=1