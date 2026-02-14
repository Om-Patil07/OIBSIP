def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

print("----- BMI Calculator -----")
weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

height = height_cm / 100   
bmi = calculate_bmi(weight, height)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are classified as Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You are classified as Normal")
elif bmi >= 25 and bmi < 30:
    print("You are classified as Overweight")
else:
    print("You are classified as Obesity")
