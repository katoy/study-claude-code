import pytest
from find_range import find_range


class TestFindRange:
    """find_range 関数のテストクラス"""

    def test_normal_list(self):
        """通常のリストで正しく動作することを確認"""
        assert find_range([1, 5, 3, 9, 2]) == 8

    def test_negative_numbers(self):
        """負の数を含むリストで正しく動作することを確認"""
        assert find_range([-5, 0, 10, 3]) == 15

    def test_single_element(self):
        """1 つの要素のリストで差が 0 であることを確認"""
        assert find_range([7]) == 0

    def test_all_same_values(self):
        """すべて同じ値のリストで差が 0 であることを確認"""
        assert find_range([5, 5, 5, 5]) == 0

    def test_float_values(self):
        """float を含むリストで正しく動作することを確認"""
        assert find_range([1.5, 3.7, 2.1]) == pytest.approx(2.2)

    def test_two_elements(self):
        """2 つの要素のリストで正しく動作することを確認"""
        assert find_range([3, 10]) == 7

    def test_large_numbers(self):
        """大きな数値で正しく動作することを確認"""
        assert find_range([1000000, 2000000]) == 1000000

    def test_empty_list_raises_error(self):
        """空のリストで ValueError が発生することを確認"""
        with pytest.raises(ValueError, match="空のリストは渡せません"):
            find_range([])

    def test_negative_range(self):
        """最小値が最大値より負の方向にある場合を確認"""
        assert find_range([-100, -50, -10]) == 90

    def test_mixed_positive_negative(self):
        """正の数と負の数が混在する場合を確認"""
        assert find_range([-10, 0, 10]) == 20
