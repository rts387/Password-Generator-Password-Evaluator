import random
import string
import math


def load_dictionary(file='word.txt'):
    with open(file, 'r') as f:
        return set(f.read().splitlines())

def contains_dictionary_word(password, dictionary):
    
    for word in dictionary:
        if word.lower() in password.lower():
            return True
    return False

def generate_password(length=12, use_digits=True, use_special=True):
 
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

def password_strength(password, dictionary):
  
    length_score = min(len(password) / 4, 1)  
    variety_score = len(set(password)) / len(password)  
    entropy = len(password) * math.log2(len(set(password)))  
    
    score = (length_score + variety_score) / 2 * 10  
    
    strength = "Weak"
    if score > 7:
        strength = "Strong"
    elif score > 5:
        strength = "Moderate"
    
    
    if contains_dictionary_word(password, dictionary):
        strength = "Weak (contains common dictionary word)"
    
    return {
        "score": round(score, 2),
        "entropy": round(entropy, 2),
        "strength": strength
    }

if __name__ == "__main__":
    dictionary = load_dictionary('word.txt')  
    
    while True:
        choice = input("Do you want to enter a password to evaluate (E), generate a new password (G), or exit (X)? ").strip().lower()
        
        if choice == 'x':
            print("Exiting program. Goodbye!")
            break
        
        if choice == 'e':
            pwd = input("Enter your password: ")
        elif choice == 'g':
            length = int(input("Enter password length: "))
            use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
            use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
            pwd = generate_password(length, use_digits, use_special)
            print(f"Generated Password: {pwd}")
        else:
            print("Invalid choice. Please enter 'E', 'G', or 'X'.")
            continue
        
        strength_info = password_strength(pwd, dictionary)
        print(f"Strength: {strength_info['strength']} (Score: {strength_info['score']}, Entropy: {strength_info['entropy']})")