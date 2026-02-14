def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


print("----- BMI Calculator -----")

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        if weight <= 0:
            print("Weight must be greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        height_cm = float(input("Enter your height in cm: "))
        if height_cm <= 0:
            print("Height must be greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

height = height_cm / 100
bmi = calculate_bmi(weight, height)

print("\n----- Result -----")
print("Weight:", weight, "kg")
print("Height:", height_cm, "cm")
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are classified as Underweight")
    print("Suggestion: Increase calorie intake and eat healthy foods.")
elif bmi >= 18.5 and bmi < 25:
    print("You are classified as Normal")
    print("Suggestion: Maintain a balanced diet and exercise regularly.")
elif bmi >= 25 and bmi < 30:
    print("You are classified as Overweight")
    print("Suggestion: Try regular workouts and avoid junk food.")
else:
    print("You are classified as Obesity")
    print("Suggestion: Consult a doctor and follow a proper diet plan.")

print("\nBMI Categories:")
print("Underweight : Below 18.5")
print("Normal      : 18.5 - 24.9")
print("Overweight  : 25 - 29.9")
print("Obesity     : 30 and above")
