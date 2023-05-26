1# 🚨 Don't change the code below 👇
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print(type(height)) to find struct type
# convert from string to float by casting
new_weight = float(weight)
new_height = float(height)

# Use parentheses to divide and ** for exponent
BMI = int(new_weight / (new_height ** 2))

print(BMI)




