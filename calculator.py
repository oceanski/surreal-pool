#planning functions

def addition(n,n2):
  a=n+n2
  return a

def subtraction(n,n2):
  b=n-n2
  return b

def multiplication(n,n2):
  c=n*n2
  return c

def division(n,n2):
  d=n/n2
  return d
  
def modulus(n,n2):
  e=n%n2
  return e

def factorial(n):
  f=1
  for i in range(n):
    f*=n
    n-=1
  return f

def exponent(n,n2):
  g=1
  for i in range(n2):
    g*=n
  return g
  
#intro and input

print("Welcome to the Python Calculator. These are the operations we offer:\n\nAddition: +\nSubtraction: -\nMutliplication: *\nDivision: /\nModulus: %\nFactorial: !\nExponent: ^")

#answers

def instructions():
  op=input("\nPlease enter the operator of the function you would like to use: ")
  n=int(input("Number 1: "))
  if op=="!":
    pass
  else:
    n2=int(input("Number 2: "))
  
  if op=="+":
    print("Result: "+str(addition(n,n2)))

  if op=="-":
    print("Result: "+str(subtraction(n,n2)))
  
  if op=="*":
    print("Result: "+str(multiplication(n,n2)))
  
  if op=="/":
    print("Result: "+str(division(n,n2)))

  if op=="%":
    print("Result: "+str(modulus(n,n2)))
  
  if op=="!":
    print("Result: "+str(factorial(n)))

  if op=="^":
    print("Result: "+str(exponent(n,n2)))

  q=input("\nWould you like to perform another operation? Enter 'Y' for yes and 'N' for no: ")
  if q=="Y":
    print(instructions())
  elif q=="N":
    print("")

instructions()
  

  