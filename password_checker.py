import re
import math
import sys

# Sample common passwords list (can be expanded)
COMMON_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "123456789", "12345",
    "1234", "111111", "1234567", "dragon", "123123", "abc123", "monkey",
    "letmein", "football", "iloveyou", "admin", "welcome"
}

def calculate_entropy(password: str) -> float:
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"\d", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32  # Approximate number of special characters
    entropy = len(password) * math.log2(charset) if charset else 0
    return entropy

def check_strength(password: str) -> str:
    length = len(password)
    entropy = calculate_entropy(password)

    # Criteria checks
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    is_common = password.lower() in COMMON_PASSWORDS

    # Scoring system
    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if length >= 12:
        score += 1
    if entropy >= 50:
        score += 1
    if is_common:
        score -= 2  # Penalize for being a common password

    # Strength evaluation
    if score <= 2:
        return "❌ Weak"
    elif 3 <= score <= 4:
        return "⚠️  Moderate"
    elif 5 <= score <= 6:
        return "✅ Strong"
    else:
        return "🔐 Very Strong"

def main():
    print("\n=== Password Strength Checker ===\n")
    try:
        password = input("Enter a password to check: ")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit()

    if not password:
        print("No password entered.")
        sys.exit()

    strength = check_strength(password)
    entropy = calculate_entropy(password)

    print(f"\nPassword strength: {strength}")
    print(f"Entropy score: {entropy:.2f} bits\n")

if __name__ == "__main__":
    main()
