import pytest
from datetime import date
from models import Transaction, TransactionType
from storage import JSONStorage

@pytest.fixture
def temp_storage(tmp_path):
    file_path = tmp_path / "test_records.json"
    return JSONStorage(str(file_path))

def test_save_and_load(temp_storage):
    transactions = [
        Transaction(
            date=date(2026, 5, 5),
            category="食費",
            amount=1200,
            transaction_type=TransactionType.EXPENSE
        ),
        Transaction(
            date=date(2026, 5, 6),
            category="趣味",
            amount=5000,
            transaction_type=TransactionType.EXPENSE
        )
    ]
    
    temp_storage.save_transactions(transactions)
    loaded = temp_storage.load_transactions()
    
    assert len(loaded) == 2
    assert loaded[0].category == "食費"
    assert loaded[1].amount == 5000
    assert loaded[0].id == transactions[0].id

def test_load_non_existent_file(tmp_path):
    file_path = tmp_path / "non_existent.json"
    storage = JSONStorage(str(file_path))
    assert storage.load_transactions() == []

def test_load_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("invalid json")
    storage = JSONStorage(str(file_path))
    assert storage.load_transactions() == []

def test_ensure_directory_creates_dir(tmp_path):
    new_dir = tmp_path / "nested" / "dir"
    file_path = new_dir / "data.json"
    assert not new_dir.exists()
    
    storage = JSONStorage(str(file_path))
    assert new_dir.exists()
    assert storage.load_transactions() == []
