while True:
    name = input("What is your name? ")
    if name.isalpha() and 1 <= len(name) <= 15:
        break
    elif len(name) > 15:
        print("Name must be no more than 15 characters. Try again.")
    elif not name.isalpha():
        print("Name must contain only letters. No numbers or special characters allowed.")
    else:
        print("Please enter a valid name.")

print(f"Hello {name}!")
print("Welcome to the Copilot Lab!")
print("This is a simple Python program that greets the user by name.")
