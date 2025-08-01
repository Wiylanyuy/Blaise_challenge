# Password Security Analyzer

# List of common passwords (20+)
COMMON_PASSWORDS = []

def analyze_password(password):
    score = 0
    feedback = []
    suggestions = []
    
    # Check length (minimum 8 characters)
    length = len(password) >= 8
    if length:
        score += 20
        feedback.append("✅ Length requirement (8+ chars)")
    else:
        feedback.append("❌ Too short (minimum 8 characters)")
        suggestions.append("Increase password length to at least 8 characters")
    
    # Checking for uppercase letters
    has_uppercase = any(c.isupper() for c in password)
    if has_uppercase:
        score += 20
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")
        suggestions.append("Add at least one uppercase letter (A-Z)")
    
    # Check for lowercase letters
    has_lowercase = any(c.islower() for c in password)
    if has_lowercase:
        score += 20
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")
        suggestions.append("Add at least one lowercase letter (a-z)")
    
    # Check for numbers
    has_number = any(c.isdigit() for c in password)
    if has_number:
        score += 20
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Missing numbers")
        suggestions.append("Add at least one number (0-9)")
    
    # Check for special characters
    special_chars = "!@#$%^&*"
    has_special_chars = any(c in special_chars for c in password)
    if has_special_chars:
        score += 20
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Missing special characters")
        suggestions.append(f"Add at least one special character ({special_chars})")
    
    # Check if password is common
    is_common = password.lower() in COMMON_PASSWORDS
    if not is_common:
        score += 20
        feedback.append("✅ Not a common password")
    else:
        feedback.append("❌ Common password detected")
        suggestions.append("Avoid using common words or number sequences")
    
    # Determine strength level
    if score <= 40:
        strength = "Weak"
    elif score <= 60:
        strength = "Fair"
    elif score <= 80:
        strength = "Good"
    elif score <= 100:
        strength = "Strong"
    else:
        strength = "Excellent"
    
    # Suggestions base on strength
    if len(suggestions) == 0 and score < 120:
        suggestions.append("Consider using a passphrase for better memorability and security")
    
    return {
        'password': password,
        'score': score,
        'strength': strength,
        'feedback': feedback,
        'suggestions': suggestions
    }

def main():
    print("=== PASSWORD SECURITY ANALYZER ===")
    password = input("Enter password your password: ")
    
    results = analyze_password(password)
    
    print("\n🔒 SECURITY ANALYSIS RESULTS")
    print(f"Password: {results['password']}")
    print(f"Score: {results['score']}/120 ({results['strength']})\n")
    
    for item in results['feedback']:
        print(item)
    
    if results['suggestions']:
        print("\n💡 SUGGESTIONS:")
        for suggestion in results['suggestions']:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()