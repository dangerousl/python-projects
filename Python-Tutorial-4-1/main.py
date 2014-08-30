

x = int(input("Enter integer:"))
y = int(input("Enter another integer:"))

l = [x,y]

if(x < y):
  print("The greater number is " + str(y) + ".")
elif(x > y):
  print("The greater number is " + str(x) + ".")
else:
  print("Those two numbers are the same value!")
