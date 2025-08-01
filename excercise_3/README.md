PASSWORD SECURITY ANALYZER
The Password Security Analyzer is a Python program that evaluates the strength of passwords based on multiple security criteria. It provides a detailed analysis of password vulnerabilities and offers specific suggestions for improvement.

FEATURES
Comprehensive Security Checks:

Minimum length requirement (8+ characters)

Presence of uppercase letters

Presence of lowercase letters

Inclusion of numbers

Use of special characters (!@#$%^&*)

Check against common passwords

Scoring System:

Each criterion worth 20 points (total 120 points max)

Clear strength rating (Weak, Fair, Good, Strong, Excellent)

Actionable Feedback:

Visual indicators of passed/failed checks (✅/❌)

Specific improvement suggestions

Common password detection

USAGE

Run the program:

bash
python password_analyzer.py
Enter the password you want to analyze when prompted

View the security analysis results and improvement suggestions

Example Output
=== PASSWORD SECURITY ANALYZER ===
Enter password your password: Wiyla77%t5sd

🔒 SECURITY ANALYSIS RESULTS
Password: Wiyla77%t5sd
Score: 120/120 (Excellent)

✅ Length requirement (8+ chars)
✅ Contains uppercase letters
✅ Contains lowercase letters
✅ Contains numbers
✅ Contains special characters
✅ Not a common password




