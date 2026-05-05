import re

def check_password_strength(password: str) -> str:
    """
    Check the strength of a password based on specific rules.

    Rules:
    - At least 8 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?/)

    Returns:
    - "弱い" (Weak): 0-1 rules met
    - "普通" (Medium): 2-3 rules met
    - "強い" (Strong): All 4 rules met

    Raises:
    - TypeError: If password is not a string.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    met_rules = 0

    # Rule 1: At least 8 characters long
    if len(password) >= 8:
        met_rules += 1

    # Rule 2: Contains both uppercase and lowercase letters
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        met_rules += 1

    # Rule 3: Contains at least one digit
    if any(c.isdigit() for c in password):
        met_rules += 1

    # Rule 4: Contains at least one special character
    # Using a broader set of special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?/]', password):
        met_rules += 1

    if met_rules <= 1:
        return "弱い"
    elif met_rules <= 3:
        return "普通"
    else:
        return "強い"
