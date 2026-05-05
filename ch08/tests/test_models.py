from datetime import date
from models import Transaction, TransactionType

def test_transaction_creation():
    t = Transaction(
        date=date(2026, 5, 5),
        category="食費",
        amount=1000,
        transaction_type=TransactionType.EXPENSE,
        note="ランチ"
    )
    assert t.category == "食費"
    assert t.amount == 1000
    assert t.transaction_type == TransactionType.EXPENSE
    assert t.note == "ランチ"
    assert t.id != ""

def test_transaction_to_dict():
    t = Transaction(
        date=date(2026, 5, 5),
        category="食費",
        amount=1000,
        transaction_type=TransactionType.EXPENSE
    )
    d = t.to_dict()
    assert d["date"] == "2026-05-05"
    assert d["transaction_type"] == "expense"
    assert d["category"] == "食費"
    assert d["amount"] == 1000

def test_transaction_from_dict():
    data = {
        "id": "test-uuid",
        "date": "2026-05-05",
        "category": "給与",
        "amount": 200000,
        "transaction_type": "income",
        "note": "5月分"
    }
    t = Transaction.from_dict(data)
    assert t.id == "test-uuid"
    assert t.date == date(2026, 5, 5)
    assert t.category == "給与"
    assert t.amount == 200000
    assert t.transaction_type == TransactionType.INCOME
    assert t.note == "5月分"
