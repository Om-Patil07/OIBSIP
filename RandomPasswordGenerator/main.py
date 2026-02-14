import string
import random

print("----- Random Password Generator -----")

while True:
    try:
        length = int(input("Enter Password Length: "))
        if length <= 0:
            print("Length must be greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

print("""Choose character set 
1. Digits
2. Lowercase Letters
3. Uppercase Letters              
4. Special Characters
5. Done""")

PasswordList = ""

while True:
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            PasswordList += string.digits
            print("Digits added")

        elif choice == 2:
            PasswordList += string.ascii_lowercase
            print("Lowercase letters added")

        elif choice == 3:
            PasswordList += string.ascii_uppercase
            print("Uppercase letters added")

        elif choice == 4:
            PasswordList += string.punctuation
            print("Special characters added")

        elif choice == 5:
            if PasswordList == "":
                print("Please select at least one character set before generating password")
            else:
                break

        else:
            print("Please enter a valid option!")

    except ValueError:
        print("Invalid input. Please enter a number.")

password = []

for i in range(length):
    RandomPassword = random.choice(PasswordList)
    password.append(RandomPassword)

final_password = "".join(password)

print("\n----- Result -----")
print("The random password is:", final_password)

if length < 6:
    print("Password Strength: Weak")
elif length >= 6 and length < 12:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

print("\nNote:")
print("Use a mix of uppercase, lowercase, digits and special characters for strong passwords.")
