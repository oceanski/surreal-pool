import random

easywords=["respect","across","another","birthday","border","branch","business","candle","careless","chocolate","continue","dangerous","different","direction","discover","general","freedom","furniture","ground","hospital","introduce","machine","million","monkey","neighbor","newspaper","partner","pleasure","photograph","substance","success","weather","wedding","vendetta"]

hardwords=["phenomenon","worcestershire","nonplussed","aberration","abstruse","archetypal","circumscribe","commensurate","diaphanous","embezzlement","grandiloquent","heterogenous","incontrovertible","multifarious","negligent","noxious","paradigm","pulchritude","sanctimonious","travesty","vicissitude"]

difficulty=input("Choose the difficulty: (Easy/Hard): ")

if difficulty=="Easy" or "easy":
  word=random.choice(easywords)
if difficulty=="Hard" or "hard":
  word=random.choice(hardwords)

wordlist=[]
blanks=[]
letters=set()
for w in word:
  blanks.append("_")
print("You have 15 guesses to figure out the correct word. Type in the entire word if you think you have guessed it. Use only lowercase letters. Good luck!")

for k in range(len(blanks)):
  print(blanks[k], sep=' ', end=' ', flush=True)
print("\n")
  
for item in word:
  wordlist.append(item)
  letters.add(item)

for i in range(15,0,-1):
  guess=input("Guess a letter/word! You have "+str(i)+" guesses remaining: ")
  if guess==word:
    for b in range(0,len(wordlist)):
      blanks[b]=wordlist[b]
  elif guess in letters:
    for j in range(0,len(wordlist)):
      if wordlist[j]==guess:
        blanks[j]=wordlist[j]
  for l in range(len(blanks)):
    print(blanks[l], sep=' ', end=' ', flush=True)
  print("\n")
  if blanks==wordlist:
    print("Congratulations! The word was '"+word+"'. It took you "+str(16-i)+" guesses.")
    break

if blanks!=wordlist:
  print("You're out of guesses! The word was "+word+".")
