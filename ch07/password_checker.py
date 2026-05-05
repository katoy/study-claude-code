import re
from enum import Enum
from dataclasses import dataclass
from typing import List

class Strength(Enum):
    WEAK = "弱い"
    MEDIUM = "普通"
    STRONG = "強い"

# Constants for configuration
MIN_LENGTH = 8
SPECIAL_CHARS_PATTERN = r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?/]'
SPECIAL_CHARS_RE = re.compile(SPECIAL_CHARS_PATTERN)

# Rule descriptions (can be moved to a separate localization file later)
RULE_DESCRIPTIONS = {
    "length": f"{MIN_LENGTH}文字以上",
    "case": "大文字と小文字の両方を含む",
    "digit": "数字を1つ以上含む",
    "special": "特殊文字を1つ以上含む"
}

@dataclass
class PasswordResult:
    strength: Strength
    met_rules: List[str]
    failed_rules: List[str]

    def __str__(self) -> str:
        return self.strength.value

def check_password_strength(password: str) -> PasswordResult:
    """
    Check the strength of a password based on specific rules.

    Rules:
    1. At least 8 characters long
    2. Contains both uppercase and lowercase letters
    3. Contains at least one digit
    4. Contains at least one special character

    Returns:
    - PasswordResult object containing strength, met rules, and failed rules.

    Raises:
    - TypeError: If password is not a string.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    rule_checks = [
        ("length", len(password) >= MIN_LENGTH),
        ("case", any(c.isupper() for c in password) and any(c.islower() for c in password)),
        ("digit", any(c.isdigit() for c in password)),
        ("special", bool(SPECIAL_CHARS_RE.search(password)))
    ]

    met_rules = [RULE_DESCRIPTIONS[key] for key, met in rule_checks if met]
    failed_rules = [RULE_DESCRIPTIONS[key] for key, met in rule_checks if not met]

    met_count = len(met_rules)

    if met_count >= 4:
        strength = Strength.STRONG
    elif met_count >= 2:
        strength = Strength.MEDIUM
    else:
        strength = Strength.WEAK

    return PasswordResult(strength, met_rules, failed_rules)

