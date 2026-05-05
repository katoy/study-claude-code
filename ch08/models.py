from dataclasses import dataclass, asdict
from datetime import date
from enum import Enum
import uuid

class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"

@dataclass
class Transaction:
    date: date
    category: str
    amount: int
    transaction_type: TransactionType
    note: str = ""
    id: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())

    def to_dict(self):
        d = asdict(self)
        d["date"] = self.date.isoformat()
        d["transaction_type"] = self.transaction_type.value
        return d

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            date=date.fromisoformat(data["date"]),
            category=data["category"],
            amount=data["amount"],
            transaction_type=TransactionType(data["transaction_type"]),
            note=data.get("note", "")
        )
