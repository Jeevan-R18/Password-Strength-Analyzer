import re
from getpass import getpass

def analyze_password_strength(password):
    # Initialize strength score and feedback
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    elif len(password) >= 6:
        score += 1
    else:
        feedback.append("Password is too short (should be at least 6 characters)")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Consider adding uppercase letters")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Consider adding lowercase letters")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Consider adding numbers")

    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 2
    else:
        feedback.append("Consider adding special characters")

    # Check for common patterns (like sequences or repeated characters)
    if (re.search(r'(.)\1{2,}', password) or  # 3 or more repeated chars
        re.search(r'123|234|345|456|567|678|789|890', password) or  # number sequences
        re.search(r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz', password.lower())):  # letter sequences
        score -= 1
        feedback.append("Avoid common patterns or sequences")

    # Determine strength level
    if score >= 7:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("Password Strength Analyzer")
    print("--------------------------")

    while True:
        password = getpass("Enter a password to analyze (or press Enter to quit): ")
        if not password:
            break

        strength, feedback = analyze_password_strength(password)

        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions to improve:")
            for item in feedback:
                print(f"- {item}")
        else:
            print("Your password meets all recommended criteria!")

        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
