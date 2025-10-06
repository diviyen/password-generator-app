import random # random variables generator
import string # a collection of string constants

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation # letters, digits and punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print("Generated password:", generate_password(length))
    
    # password generator app