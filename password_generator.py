import random
import string


def generate_password(length, use_digits=True, use_symbols=True):
    
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    
    all_characters = letters + digits + symbols

    if not all_characters:
        return "Error: No character types selected."

    
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password


def main():
    print("=== TASK 3: PASSWORD GENERATOR ===")

    
    try:
        length = int(
            input("Enter the desired length of the password (e.g., 12): ")
        )
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return


    print("\nSelect Complexity Level:")
    include_digits = (
        input("Include numbers? (y/n): ").strip().lower() == "y"
    )
    include_symbols = (
        input("Include special characters/symbols? (y/n): ").strip().lower()
        == "y"
    )

    
    password = generate_password(
        length, use_digits=include_digits, use_symbols=include_symbols
    )

   
    print("\n" + "=" * 35)
    print(f"Generated Password: {password}")
    print("=" * 35)


if __name__ == "__main__":
    main()