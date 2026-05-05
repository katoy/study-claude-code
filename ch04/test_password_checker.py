import pytest
from password_checker import check_password_strength

@pytest.mark.parametrize("password, expected", [
    # 弱い (0-1 rules)
    ("", "弱い"),            # 0 rules
    ("abc", "弱い"),         # 0 rules (only lower)
    ("A", "弱い"),           # 0 rules (only upper)
    ("1", "弱い"),           # 1 rule (digit)
    ("!", "弱い"),           # 1 rule (special)
    ("abcdefg", "弱い"),     # 0 rules (length 7, only lower)
    
    # 普通 (2-3 rules)
    ("Abcdefgh", "普通"),    # length >= 8, upper+lower (2 rules)
    ("Abcdef1", "普通"),     # upper+lower, digit (2 rules) - length 7
    ("abcdef1!", "普通"),    # length >= 8, digit, special (3 rules) - no upper
    ("ABCDEF1!", "普通"),    # length >= 8, digit, special (3 rules) - no lower
    ("Ab1!", "普通"),        # upper+lower, digit, special (3 rules) - short
    ("Password", "普通"),    # length >= 8, upper+lower (2 rules)
    ("_Plus12", "普通"),     # length 7, upper+lower, digit, special (3 rules)
    
    # 強い (4 rules)
    ("Abcdef1!", "強い"),
    ("LongPassword123#", "強い"),
    ("P@ssw0rd2024", "強い"),
    ("uP8+lower", "強い"),
])
def test_password_strength(password, expected):
    assert check_password_strength(password) == expected

def test_invalid_input():
    with pytest.raises(TypeError):
        check_password_strength(None)
    with pytest.raises(TypeError):
        check_password_strength(123)

@pytest.mark.parametrize("special_char", list("!@#$%^&*()_+-=[]{}|;:,.<>?/"))
def test_all_special_chars(special_char):
    # Base: "Ab1" (upper, lower, digit) + special_char
    # This meets 4 rules: length 4 (fail), upper+lower (pass), digit (pass), special (pass)
    # Wait, length 4 fails. So it meets 3 rules -> "普通"
    assert check_password_strength(f"Ab1{special_char}") == "普通"
    # To get "強い", need length >= 8
    assert check_password_strength(f"Ab12345{special_char}") == "強い"
