import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    all_chars = letters + digits + special_chars

    if length < 4:
        return "Password length must be at least 4 characters."

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Password Generator")
    print("-------------------")
    try:
        length = int(input("Enter the desired length of your password: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
