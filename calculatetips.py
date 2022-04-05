# enter tip
num = float(input("Enter total bill amount, in dollars: "))
# enter percent tip
tip_percent = float(input("Enter the percent you would like to tip, as a decimal: "))
# recognize invalid entries
if tip_percent > 1 or tip_percent < 0:
  print("Invalid input. Please enter percent as a decimal.")
# calculate tip and print tip + total bill
tip_dollar = (num*tip_percent)
print("Your tip, rounded to the nearest dollar: " , int(tip_dollar))
print("Your tip, rounded to the nearest cent: " , str("%.2f" % tip_dollar))
print("Your total bill, including the tip: " , float(num + tip_dollar))