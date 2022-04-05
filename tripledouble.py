player1=[0,0,0]
player2=[0,0,0]
player3=[0,0,0]
player4=[0,0,0]
player5=[0,0,0]
allplayers=[player1,player2,player3,player4,player5]
print(allplayers)
print("\n")

p1point=int(input("Enter player 1's points: "))
p1rebound=int(input("Enter player 1's rebounds: "))
p1assist=int(input("Enter player 1's assists: "))
player1[0]=p1point
player1[1]=p1rebound
player1[2]=p1assist
print(allplayers)
print("\n")

p2point=int(input("Enter player 2's points: "))
p2rebound=int(input("Enter player 2's rebounds: "))
p2assist=int(input("Enter player 2's assists: "))
player2[0]=p2point
player2[1]=p2rebound
player2[2]=p2assist
print(allplayers)
print("\n")

p3point=int(input("Enter player 3's points: "))
p3rebound=int(input("Enter player 3's rebounds: "))
p3assist=int(input("Enter player 3's assists: "))
player3[0]=p3point
player3[1]=p3rebound
player3[2]=p3assist
print(allplayers)
print("\n")

p4point=int(input("Enter player 4's points: "))
p4rebound=int(input("Enter player 4's rebounds: "))
p4assist=int(input("Enter player 4's assists: "))
player4[0]=p4point
player4[1]=p4rebound
player4[2]=p4assist
print(allplayers)
print("\n")

p5point=int(input("Enter player 5's points: "))
p5rebound=int(input("Enter player 5's rebounds: "))
p5assist=int(input("Enter player 5's assists: "))
player5[0]=p5point
player5[1]=p5rebound
player5[2]=p5assist
print(allplayers)
print("\n")

print("The final data:")
print(allplayers)

if player1[0]>10 and player1[1]>10 and player1[2]>10:
  print("Player 1 had a triple double!")
if player2[0]>10 and player2[1]>10 and player2[2]>10:
  print("Player 2 had a triple double!")
if player3[0]>10 and player3[1]>10 and player3[2]>10:
  print("Player 3 had a triple double!")
if player4[0]>10 and player4[1]>10 and player4[2]>10:
  print("Player 4 had a triple double!")
if player5[0]>10 and player5[1]>10 and player5[2]>10:
  print("Player 5 had a triple double!")
