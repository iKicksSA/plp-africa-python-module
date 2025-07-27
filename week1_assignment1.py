num1 = int ( input ("Enter the first number: "))

num2 = int ( input ("Enter the second number: "))

operation = input("Enter a mathematical operation ( + , - , * , or / ).")

if operation == "+":
  results = num1 + num2

  print(f"{num1} + {num2} = {results}.")

elif operation == "-":
  results = num1 - num2

  print(f"{num1} - {num2} = {results}.")

elif operation == "*":
  results = num1 * num2

  print(f"{num1} * {num2} = {results}.")

elif operation == "/":

  if num2 == 0:
    print("Cannot divide with ZERO!")

  else:
   results = num1 // num2

   print(f"{num1} / {num2} = {results}.")

else:
  print("Invalid operation entered! ")
