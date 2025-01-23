import random
import string

def generate_password(length, complexity):
    # Define different character sets based on complexity
    if complexity == 1:
        # Lowercase letters only
        characters = string.ascii_lowercase
    elif complexity == 2:
        # Lowercase + Uppercase letters
        characters = string.ascii_letters
    elif complexity == 3:
        # Lowercase + Uppercase letters + Digits
        characters = string.ascii_letters + string.digits
    elif complexity == 4:
        # Lowercase + Uppercase letters + Digits + Special characters
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level!"
    
    # Randomly select characters from the specified character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def password_generator():
    print("Welcome to the Password Generator!")

    while True:
        try:
            # Prompt for password length
            length = int(input("Enter the desired password length: "))
            if length < 8:
                print("Password length should be at least 8 characters for security.")
                continue

            # Prompt for complexity level
            print("\nSelect the password complexity level:")
            print("1. Lowercase letters only")
            print("2. Lowercase + Uppercase letters")
            print("3. Lowercase + Uppercase letters + Digits")
            print("4. Lowercase + Uppercase letters + Digits + Special characters")
            complexity = int(input("Choose complexity level (1/2/3/4): "))
            
            if complexity < 1 or complexity > 4:
                print("Invalid complexity level! Please choose between 1 and 4.")
                continue

            # Generate the password
            password = generate_password(length, complexity)

            # Display the generated password
            print(f"\nGenerated Password: {password}")
            
            # Ask if user wants to generate another password
            another = input("\nDo you want to generate another password? (yes/no): ").lower()
            if another != 'yes':
                print("Exiting Password Generator. Stay secure!")
                break
        except ValueError:
            print("Invalid input! Please enter numeric values for length and complexity.")

if __name__ == "__main__":
    password_generator()
