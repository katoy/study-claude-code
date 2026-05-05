import re

# Constants for configuration
MIN_LENGTH = 8
SPECIAL_CHARS_PATTERN = r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?/]'

def check_password_strength(password: str) -> str:
    """
    Check the strength of a password based on specific rules.

    Rules:
    - At least 8 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character

    Returns:
    - "弱い" (Weak): 0-1 rules met
    - "普通" (Medium): 2-3 rules met
    - "強い" (Strong): All 4 rules met

    Raises:
    - TypeError: If password is not a string.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    # Evaluate all rules as a list of booleans
    rules = [
        len(password) >= MIN_LENGTH,
        any(c.isupper() for c in password) and any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        bool(re.search(SPECIAL_CHARS_PATTERN, password))
    ]

    # Count how many rules are satisfied
    met_count = sum(rules)

    # Determine strength based on the count
    if met_count >= 4:
        return "強い"
    if met_count >= 2:
        return "普通"
    return "弱い"
