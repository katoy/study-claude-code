import pytest
from password_checker import check_password_strength, Strength, RULE_DESCRIPTIONS

@pytest.mark.parametrize("password, expected", [
    # 弱い (0-1 rules)
    ("", Strength.WEAK),            # 0 rules
    ("abc", Strength.WEAK),         # 0 rules (only lower)
    ("A", Strength.WEAK),           # 0 rules (only upper)
    ("1", Strength.WEAK),           # 1 rule (digit)
    ("!", Strength.WEAK),           # 1 rule (special)
    ("abcdefg", Strength.WEAK),     # 0 rules (length 7, only lower)
    
    # 普通 (2-3 rules)
    ("Abcdefgh", Strength.MEDIUM),    # length >= 8, upper+lower (2 rules)
    ("Abcdef1", Strength.MEDIUM),     # upper+lower, digit (2 rules) - length 7
    ("abcdef1!", Strength.MEDIUM),    # length >= 8, digit, special (3 rules) - no upper
    ("ABCDEF1!", Strength.MEDIUM),    # length >= 8, digit, special (3 rules) - no lower
    ("Ab1!", Strength.MEDIUM),        # upper+lower, digit, special (3 rules) - short
    ("Password", Strength.MEDIUM),    # length >= 8, upper+lower (2 rules)
    ("_Plus12", Strength.MEDIUM),     # length 7, upper+lower, digit, special (3 rules)
    
    # 強い (4 rules)
    ("Abcdef1!", Strength.STRONG),
    ("LongPassword123#", Strength.STRONG),
    ("P@ssw0rd2024", Strength.STRONG),
    ("uP8+lower", Strength.STRONG),
])
def test_password_strength(password, expected):
    result = check_password_strength(password)
    assert result.strength == expected
    assert str(result) == expected.value

def test_invalid_input():
    with pytest.raises(TypeError):
        check_password_strength(None)
    with pytest.raises(TypeError):
        check_password_strength(123)

@pytest.mark.parametrize("special_char", list("!@#$%^&*()_+-=[]{}|;:,.<>?/"))
def test_all_special_chars(special_char):
    # Base: "Ab1" (upper, lower, digit) + special_char
    # This meets 3 rules: upper+lower, digit, special (no length) -> Strength.MEDIUM
    result_short = check_password_strength(f"Ab1{special_char}")
    assert result_short.strength == Strength.MEDIUM
    assert RULE_DESCRIPTIONS["special"] in result_short.met_rules

    # To get Strength.STRONG, need length >= 8
    result_long = check_password_strength(f"Ab12345{special_char}")
    assert result_long.strength == Strength.STRONG
    assert RULE_DESCRIPTIONS["special"] in result_long.met_rules

def test_detailed_feedback():
    result = check_password_strength("abc")
    assert RULE_DESCRIPTIONS["length"] in result.failed_rules
    assert RULE_DESCRIPTIONS["case"] in result.failed_rules
    assert RULE_DESCRIPTIONS["digit"] in result.failed_rules
    assert RULE_DESCRIPTIONS["special"] in result.failed_rules
    assert len(result.met_rules) == 0
