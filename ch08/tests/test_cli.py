import pytest
from unittest.mock import patch
from datetime import date
from storage import JSONStorage
from cli import record_transaction
from models import TransactionType
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

def test_cli_main_block():
    from unittest.mock import patch
    
    # runpy.run_path を使用して cli.py をスクリプトとして実行する
    # これにより coverage が cli.py のファイルパスに関連付けられる
    # 副作用を抑えるために JSONStorage と print をモックし、
    # input は日付エラーで即終了するように設定する
    with patch("storage.JSONStorage"), \
         patch("builtins.print"), \
         patch("builtins.input", side_effect=["invalid-date"]):
        
        # run_name="__main__" で実行することで if __name__ == "__main__": ブロックを通過
        runpy.run_path("cli.py", run_name="__main__")
        
        # 実行が正常に終了すること（例外が起きないこと）を確認
