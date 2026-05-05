import json
import os
from typing import List
from models import Transaction

class JSONStorage:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._ensure_directory()

    def _ensure_directory(self):
        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def load_transactions(self) -> List[Transaction]:
        if not os.path.exists(self.file_path):
            return []
        
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Transaction.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            return []

    def save_transactions(self, transactions: List[Transaction]):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in transactions], f, indent=2, ensure_ascii=False)
