# read in states 
f = open("states.txt")
data = f.readlines()
states = [line.strip() for line in data]
f.close()

# read in capitals
f = open("capitals.txt")
data = f.readlines()
capitals = [line.strip() for line in data]
f.close()

import random

statecap={}
score=0

# create a dictionary to match the states with the capitals
for i in range(len(states)):
  statecap[states[i]]=capitals[i]

# change the order of the states so the questions are generated randomly
for j in states:
  random.shuffle(states)

# questions + verification of answers
for k in range(len(states)):
  ans=input("What is the capital of "+states[k]+"? ")
  if ans==statecap[states[k]]:
    print("Correct!")
    score+=1
  else:
    print("Incorrect! Your total score is: "+str(score))
    break
