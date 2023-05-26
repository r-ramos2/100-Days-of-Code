print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride!")
  age = int(input("Enter your age: "))
  if age < 12:
    bill = 5
    print("Children pay $5")
  elif age < 18:
    bill = 7
    print("Teenagers pay $7")
  elif age >= 45 and age <= 55:
    bill = 0
    print("You ride for free!")
  else:
    bill = 12
    print("Adults pay $12")

  wants_photo = input("Would you like a photo? Y/N ")
  if wants_photo == "Y":
    bill += 3
  print(f"Your total to pay is ${bill}")
else:
  print("You can't ride!")
  