import random
import string
import re

def generate_redeem_code():
    """Generate a random Google Play redeem code."""
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choices(characters, k=16))
    formatted_code = f"{code[:4]}-{code[4:8]}-{code[8:12]}-{code[12:]}"
    return formatted_code

def is_valid_code(code):
    """Check if the redeem code is in the correct format."""
    pattern = r'^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$'
    return re.match(pattern, code) is not None

def main():
    num_codes = int(input("Enter the number of redeem codes to generate: "))
    codes = [generate_redeem_code() for _ in range(num_codes)]
    
    print("\nGenerated Redeem Codes:")
    for code in codes:
        print(code)
    
    print("\nValidating Redeem Codes:")
    for code in codes:
        if is_valid_code(code):
            print(f"{code} - Format is valid")
        else:
            print(f"{code} - Format is invalid")

if __name__ == "__main__":
    main()
