import re

def detect_phishing(email_file):
    with open(email_file, 'r') as f:
        email_content = f.read()

    # Common phishing and security indicators
    phishing_indicators = [
        r'urgent|important|verify|account|login|password|suspicious|confirm|alert|security|unauthorized',
        r'dear\s+[a-zA-Z]+',
        r'http[s]?://[^\s<>"]+|www\.[^\s<>"]+',
        r'\b\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\b'  # Matches credit card numbers
    ]

    security_indicators = [
        r'phishing|malware|virus|suspicious activity|suspicious link|suspicious attachment|unauthorized access',
        r'password reset|account compromise|fraudulent activity|data breach|security breach',
        r'2fa|two-factor authentication|multi-factor authentication|phishing awareness training'
    ]

    phishing_count = 0
    for indicator in phishing_indicators:
        matches = re.findall(indicator, email_content, re.IGNORECASE)
        if matches:
            print(f"Phishing indicator found: {matches}")
            phishing_count += len(matches)

    security_count = 0
    for indicator in security_indicators:
        matches = re.findall(indicator, email_content, re.IGNORECASE)
        if matches:
            print(f"Security indicator found: {matches}")
            security_count += len(matches)

    if phishing_count > 0:
        print(f"Phishing detected! Found {phishing_count} phishing indicators.")
    else:
        print("No phishing indicators found.")

    if security_count > 0:
        print(f"Security concerns detected! Found {security_count} security indicators.")
    else:
        print("No security indicators found.")

if __name__ == "__main__":
    email_file = input("Enter the path to the saved email file: ")
    detect_phishing(email_file)
