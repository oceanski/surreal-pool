password = input("Create a password: ")
guess = str(input("Enter the password: "))
i=1
while i<5 and guess != password:
  guess = input("Incorrect password. Try again: ")
  i+=1
if i>4 and guess != password:
  print("Too many incorrect tries. System locked.")
if guess == password:
  print("System unlocked! It took you " + str(i) + " tries.")