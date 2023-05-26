# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

number_items = len(names) - 1 # We start counting at 0
random_number = random.randint(0, number_items)
print(random_number)

# random_name = random.choice(names)
# print(f"This person will pay for the meal: {random_name}")
