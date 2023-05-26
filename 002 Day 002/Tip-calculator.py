#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_people = float(input("How many people to split the bill? "))

new_percentage_tip = 1 + percentage_tip / 100
computation = (total_bill * new_percentage_tip) / number_people
solution = "{:.2f}".format(computation)

print(f"Each person should pay: ${solution}")