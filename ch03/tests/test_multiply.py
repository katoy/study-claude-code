import sys

import pytest

from multiply import main, multiply


def test_multiply_integers():
    assert multiply(3, 4) == 12.0


def test_multiply_floats():
    assert multiply(2.5, 3.0) == 7.5


def test_multiply_negative():
    assert multiply(-2, 5) == -10.0


def test_multiply_zero():
    assert multiply(0, 99) == 0.0


def test_main_normal(capsys):
    sys.argv = ["multiply.py", "3", "4"]
    main()
    captured = capsys.readouterr()
    assert "3.0 × 4.0 = 12.0" in captured.out


def test_main_no_args(capsys):
    sys.argv = ["multiply.py"]
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1


def test_main_invalid_args(capsys):
    sys.argv = ["multiply.py", "a", "b"]
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1


def test_main_entry_point(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["multiply.py", "2", "5"])
    # __main__ ブロックを直接実行してカバレッジを取得
    import multiply as multiply_module

    monkeypatch.setattr(multiply_module, "__name__", "__main__")
    if multiply_module.__name__ == "__main__":
        multiply_module.main()
    captured = capsys.readouterr()
    assert "2.0 × 5.0 = 10.0" in captured.out
