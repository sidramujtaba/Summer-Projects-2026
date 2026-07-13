# Import built-in modules
import string      # Used to get letters (a-z, A-Z) and digits (0-9)
import getpass     # Used to hide the password while typing


# Function to check the password strength
def check_pwd():

    # Ask the user to enter a password (hidden on screen)
    password = getpass.getpass("Enter the password: ")

    # Variable to store password strength score
    strength = 0

    # Variable to store the final remark
    remarks = ""

    # Initialize all counters to zero
    lower_count = upper_count = num_count = wspace_count = specialcharacter_count = 0


    # Go through each character of the password
    for char in password:

        # Check if it is a lowercase letter
        if char in string.ascii_lowercase:
            lower_count += 1

        # Check if it is an uppercase letter
        elif char in string.ascii_uppercase:
            upper_count += 1

        # Check if it is a number
        elif char in string.digits:
            num_count += 1

        # Check if it is a space
        elif char == " ":
            wspace_count += 1

        # Otherwise, it is a special character
        else:
            specialcharacter_count += 1


    # Increase strength if at least one lowercase letter exists
    if lower_count >= 1:
        strength += 1

    # Increase strength if at least one uppercase letter exists
    if upper_count >= 1:
        strength += 1

    # Increase strength if at least one number exists
    if num_count >= 1:
        strength += 1

    # Increase strength if at least one space exists
    if wspace_count >= 1:
        strength += 1

    # Increase strength if at least one special character exists
    if specialcharacter_count >= 1:
        strength += 1


    # Decide the password remark based on the score

    if strength == 1:
        remarks = "Very Weak Password"

    elif strength == 2:
        remarks = "Not Good Password"

    elif strength == 3:
        remarks = "Weak Password"

    elif strength == 4:
        remarks = "Hard Password"

    elif strength == 5:
        remarks = "Very Strong Password"

    # If nothing matches
    else:
        remarks = "Very Weak Password"


    # Display the results
    print("\nYour password has:")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numbers")
    print(f"{wspace_count} whitespace characters")
    print(f"{specialcharacter_count} special characters")

    # Display the final strength score and remark
    print(f"\nPassword Strength: {strength}/5")
    print(f"Hint: {remarks}")
def ask_pwd():
    while True:
        choice = input("\nDo you want to check a password? (y/n): ")

        if choice.lower() == "y":
            return True

        elif choice.lower() == "n":
            return False

        else:
            print("Invalid input. Try again.")



# Starting point of the program
if __name__ == "__main__":

    # Welcome message
    print("+++ Welcome to Password Checker +++")

    # Keep running until the user chooses to stop
    while ask_pwd():

        # Check the password strength
        check_pwd()   #py .\main.py