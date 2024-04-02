def detect_suspicious_logins(user, threshold=5):
    """
    Check for suspicious login attempts.
    If the user exceeds the specified threshold, trigger an investigation.
    """
    login_attempts = get_login_attempts(user)
    if login_attempts >= threshold:
        trigger_investigation(user)
        print(f"Suspicious login attempts detected for user {user}. Investigation initiated.")

def get_login_attempts(user):
    """
    Placeholder function to retrieve the number of login attempts for the specified user.
    Replace with actual data retrieval logic (e.g., query logs, authentication logs).
    """
    # Simulate login attempts (replace with real logic)
    return 7

def trigger_investigation(user):
    """
    Placeholder function to trigger an investigation for the specified user.
    Replace with actual incident response actions (e.g., notify SOC, collect evidence).
    """
    # Simulate investigation (replace with real logic)
    print(f"Investigation initiated for user {user}.")

# Example usage
suspicious_user = "john.doe"
detect_suspicious_logins(suspicious_user)
