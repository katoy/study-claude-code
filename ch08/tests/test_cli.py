import pytest
from unittest.mock import patch
from datetime import date
from storage import JSONStorage
from cli import record_transaction, show_category_report, show_monthly_report, main
from models import Transaction, TransactionType
import runpy

@pytest.fixture
def temp_storage(tmp_path):
    file_path = tmp_path / "test_cli_records.json"
    return JSONStorage(str(file_path))

def test_record_income(temp_storage):
    # 入力: 日付(デフォルト), 1(収入), 給与, 200000, ボーナス
    inputs = ["", "1", "給与", "200000", "ボーナス"]
    
    with patch("builtins.input", side_effect=inputs):
        record_transaction(temp_storage)
    
    loaded = temp_storage.load_transactions()
    assert len(loaded) == 1
    assert loaded[0].transaction_type == TransactionType.INCOME
    assert loaded[0].category == "給与"
    assert loaded[0].amount == 200000
    assert loaded[0].note == "ボーナス"

def test_record_expense(temp_storage):
    # 入力: 2026-05-10, 2(支出), 食費, 1500, ランチ
    inputs = ["2026-05-10", "2", "食費", "1500", "ランチ"]
    
    with patch("builtins.input", side_effect=inputs):
        record_transaction(temp_storage)
    
    loaded = temp_storage.load_transactions()
    assert len(loaded) == 1
    assert loaded[0].transaction_type == TransactionType.EXPENSE
    assert loaded[0].date == date(2026, 5, 10)
    assert loaded[0].amount == 1500

def test_record_negative_amount_error(temp_storage, capsys):
    # 入力: デフォルト日付, 2(支出), 雑費, -500(エラー), 500, メモ
    inputs = ["", "2", "雑費", "-500", "500", "メモ"]
    
    with patch("builtins.input", side_effect=inputs):
        record_transaction(temp_storage)
    
    captured = capsys.readouterr()
    assert "エラー: 金額に負の値を入力することはできません。" in captured.out
    
    loaded = temp_storage.load_transactions()
    assert len(loaded) == 1
    assert loaded[0].amount == 500

def test_record_invalid_date(temp_storage, capsys):
    inputs = ["invalid-date"]
    with patch("builtins.input", side_effect=inputs):
        record_transaction(temp_storage)
    captured = capsys.readouterr()
    assert "エラー: 日付の形式が正しくありません。" in captured.out

def test_record_invalid_type(temp_storage, capsys):
    inputs = ["", "3"] # 1 or 2 以外
    with patch("builtins.input", side_effect=inputs):
        record_transaction(temp_storage)
    captured = capsys.readouterr()
    assert "エラー: 1 または 2 を入力してください。" in captured.out

def test_record_missing_category(temp_storage, capsys):
    inputs = ["", "1", ""] # カテゴリ空
    with patch("builtins.input", side_effect=inputs):
        record_transaction(temp_storage)
    captured = capsys.readouterr()
    assert "エラー: カテゴリは必須です。" in captured.out

def test_record_invalid_amount_format(temp_storage, capsys):
    inputs = ["", "1", "カテゴリ", "abc", "100", "メモ"]
    with patch("builtins.input", side_effect=inputs):
        record_transaction(temp_storage)
    captured = capsys.readouterr()
    assert "エラー: 金額は数値で入力してください。" in captured.out

def test_show_category_report_empty(temp_storage, capsys):
    show_category_report(temp_storage)
    captured = capsys.readouterr()
    assert "データがありません。" in captured.out

def test_show_category_report(temp_storage, capsys):
    txns = [
        Transaction(date(2026, 5, 1), "食費", 1000, TransactionType.EXPENSE),
        Transaction(date(2026, 5, 2), "食費", 2000, TransactionType.EXPENSE),
        Transaction(date(2026, 5, 1), "給与", 200000, TransactionType.INCOME),
    ]
    temp_storage.save_transactions(txns)

    show_category_report(temp_storage)
    captured = capsys.readouterr()
    assert "食費: 3000円" in captured.out
    assert "給与: 200000円" in captured.out

def test_show_category_report_no_expense(temp_storage, capsys):
    # 収入のみ、支出がないケース
    txns = [Transaction(date(2026, 5, 1), "給与", 200000, TransactionType.INCOME)]
    temp_storage.save_transactions(txns)

    show_category_report(temp_storage)
    captured = capsys.readouterr()
    assert "[支出]" in captured.out
    assert "記録なし" in captured.out
    assert "給与: 200000円" in captured.out

def test_show_category_report_no_income(temp_storage, capsys):
    # 支出のみ、収入がないケース
    txns = [Transaction(date(2026, 5, 1), "食費", 1000, TransactionType.EXPENSE)]
    temp_storage.save_transactions(txns)

    show_category_report(temp_storage)
    captured = capsys.readouterr()
    assert "[収入]" in captured.out
    assert "記録なし" in captured.out
    assert "食費: 1000円" in captured.out

def test_show_monthly_report_empty(temp_storage, capsys):
    show_monthly_report(temp_storage)
    captured = capsys.readouterr()
    assert "データがありません。" in captured.out

def test_show_monthly_report(temp_storage, capsys):
    txns = [
        Transaction(date(2026, 5, 1), "食費", 1000, TransactionType.EXPENSE),
        Transaction(date(2026, 6, 1), "食費", 1500, TransactionType.EXPENSE),
        Transaction(date(2026, 5, 15), "給与", 200000, TransactionType.INCOME),
    ]
    temp_storage.save_transactions(txns)
    
    show_monthly_report(temp_storage)
    captured = capsys.readouterr()
    assert "2026-05:" in captured.out
    assert "収入: 200000円" in captured.out
    assert "支出: 1000円" in captured.out
    assert "2026-06:" in captured.out
    assert "支出: 1500円" in captured.out

def test_main_menu_exit(capsys):
    with patch("builtins.input", side_effect=["4"]), \
         patch("storage.JSONStorage.load_transactions", return_value=[]):
        main()
    captured = capsys.readouterr()
    assert "プログラムを終了します。" in captured.out

def test_main_menu_invalid_choice(capsys):
    # 無効な選択肢(数字外) -> 終了
    with patch("builtins.input", side_effect=["abc", "4"]), \
         patch("storage.JSONStorage.load_transactions", return_value=[]):
        main()
    captured = capsys.readouterr()
    assert "エラー: 1〜4の数値を入力してください。" in captured.out

def test_main_menu_invalid_number_choice(capsys):
    # 無効な選択肢(範囲外の数字) -> 終了
    with patch("builtins.input", side_effect=["9", "4"]), \
         patch("storage.JSONStorage.load_transactions", return_value=[]):
        main()
    captured = capsys.readouterr()
    assert "エラー: 1〜4の数値を入力してください。" in captured.out

def test_main_menu_calls_record(temp_storage):
    # 記録(1) -> 終了(4)
    # record_transaction 内の入力も必要
    inputs = ["1", "2026-05-01", "2", "食費", "1000", "", "4"]
    with patch("builtins.input", side_effect=inputs), \
         patch("cli.JSONStorage", return_value=temp_storage):
        main()

    loaded = temp_storage.load_transactions()
    assert len(loaded) == 1
    assert loaded[0].category == "食費"

def test_main_menu_calls_category_report(temp_storage, capsys):
    # カテゴリ集計(2) -> 終了(4)
    txns = [Transaction(date(2026, 5, 1), "食費", 1000, TransactionType.EXPENSE)]
    temp_storage.save_transactions(txns)

    with patch("builtins.input", side_effect=["2", "4"]), \
         patch("cli.JSONStorage", return_value=temp_storage):
        main()

    captured = capsys.readouterr()
    assert "食費: 1000円" in captured.out

def test_main_menu_calls_monthly_report(temp_storage, capsys):
    # 月別レポート(3) -> 終了(4)
    txns = [Transaction(date(2026, 5, 1), "食費", 1000, TransactionType.EXPENSE)]
    temp_storage.save_transactions(txns)

    with patch("builtins.input", side_effect=["3", "4"]), \
         patch("cli.JSONStorage", return_value=temp_storage):
        main()

    captured = capsys.readouterr()
    assert "2026-05:" in captured.out

def test_cli_main_block():
    # if __name__ == "__main__": ブロックが正常に実行されることを確認
    with patch("builtins.input", side_effect=["4"]):
        runpy.run_path("cli.py", run_name="__main__")
