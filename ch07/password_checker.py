import re
from enum import Enum
from dataclasses import dataclass
from typing import List

class Strength(Enum):
    WEAK = "弱い"
    MEDIUM = "普通"
    STRONG = "強い"

# 設定用の定数
MIN_LENGTH = 8
SPECIAL_CHARS_PATTERN = r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?/]'
SPECIAL_CHARS_RE = re.compile(SPECIAL_CHARS_PATTERN)

# ルールの説明（後で別のローカライズファイルに移動可能）
RULE_DESCRIPTIONS = {
    "length": f"{MIN_LENGTH} 文字以上",
    "case": "大文字と小文字の両方を含む",
    "digit": "数字を 1 つ以上含む",
    "special": "特殊文字を 1 つ以上含む"
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
    特定のルールに基づいてパスワードの強度をチェックします。

    ルール:
    1. 少なくとも 8 文字以上
    2. 大文字と小文字の両方を含む
    3. 少なくとも 1 つ以上の数字を含む
    4. 少なくとも 1 つ以上の特殊文字を含む

    戻り値:
    - 強度、満たされたルール、および失敗したルールを含む PasswordResult オブジェクト。

    例外:
    - TypeError: パスワードが文字列でない場合。
    """
    if not isinstance(password, str):
        raise TypeError("パスワードは文字列である必要があります")

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
