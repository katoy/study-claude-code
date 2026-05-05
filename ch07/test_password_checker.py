import pytest
from password_checker import check_password_strength, Strength, RULE_DESCRIPTIONS

@pytest.mark.parametrize("password, expected", [
    # 弱い (0-1 つのルールに適合)
    ("", Strength.WEAK),            # 0 ルール
    ("abc", Strength.WEAK),         # 0 ルール (小文字のみ)
    ("A", Strength.WEAK),           # 0 ルール (大文字のみ)
    ("1", Strength.WEAK),           # 1 ルール (数字)
    ("!", Strength.WEAK),           # 1 ルール (特殊文字)
    ("abcdefg", Strength.WEAK),     # 0 ルール (長さ 7 文字、小文字のみ)
    
    # 普通 (2-3 つのルールに適合)
    ("Abcdefgh", Strength.MEDIUM),    # 長さ 8 文字以上、大文字+小文字 (2 ルール)
    ("Abcdef1", Strength.MEDIUM),     # 大文字+小文字、数字 (2 ルール) - 長さ 7 文字
    ("abcdef1!", Strength.MEDIUM),    # 長さ 8 文字以上、数字、特殊文字 (3 ルール) - 大文字なし
    ("ABCDEF1!", Strength.MEDIUM),    # 長さ 8 文字以上、数字、特殊文字 (3 ルール) - 小文字なし
    ("Ab1!", Strength.MEDIUM),        # 大文字+小文字、数字、特殊文字 (3 ルール) - 短い
    ("Password", Strength.MEDIUM),    # 長さ 8 文字以上、大文字+小文字 (2 ルール)
    ("_Plus12", Strength.MEDIUM),     # 長さ 7 文字、大文字+小文字、数字、特殊文字 (3 ルール)
    
    # 強い (4 つ全てのルールに適合)
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
    # 基本: "Ab1" (大文字、小文字、数字) + 特殊文字
    # これは 3 つのルールに適合: 大文字+小文字、数字、特殊文字 (長さ不足) -> Strength.MEDIUM
    result_short = check_password_strength(f"Ab1{special_char}")
    assert result_short.strength == Strength.MEDIUM
    assert RULE_DESCRIPTIONS["special"] in result_short.met_rules

    # 強度を STRONG にするには、長さ 8 文字以上が必要
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
