import unittest
from password_checker import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    def test_weak_passwords(self):
        # 0 rules met (too short, no upper, no lower, no digit, no special - but lower is present)
        # Actually "abc" has lower, so it meets 0 rules if we count "upper AND lower" as one rule?
        # Rule 1: length >= 8
        # Rule 2: upper and lower
        # Rule 3: digit
        # Rule 4: special
        
        self.assertEqual(check_password_strength("abc"), "弱い")  # Only 'lower' is present. Rule 2 fails because no 'upper'.
        self.assertEqual(check_password_strength(""), "弱い")     # 0 rules
        self.assertEqual(check_password_strength("A"), "弱い")    # 0 rules (only upper, no lower)
        self.assertEqual(check_password_strength("1"), "弱い")    # 1 rule (digit)
        self.assertEqual(check_password_strength("!"), "弱い")    # 1 rule (special)

    def test_medium_passwords(self):
        # 2-3 rules
        self.assertEqual(check_password_strength("Abcdefgh"), "普通") # length >= 8, upper+lower (2 rules)
        self.assertEqual(check_password_strength("Abcdef1"), "普通")  # upper+lower, digit (2 rules) - length 7
        self.assertEqual(check_password_strength("abcdef1!"), "普通") # length >= 8, digit, special (3 rules) - no upper
        self.assertEqual(check_password_strength("ABCDEF1!"), "普通") # length >= 8, digit, special (3 rules) - no lower
        self.assertEqual(check_password_strength("Ab1!"), "普通")     # upper+lower, digit, special (3 rules) - short

    def test_strong_passwords(self):
        # 4 rules
        self.assertEqual(check_password_strength("Abcdef1!"), "強い")
        self.assertEqual(check_password_strength("LongPassword123#"), "強い")

if __name__ == "__main__":
    unittest.main()
