# Password Strength Checker

Pythonでパスワードの強度をチェックするシンプルなツールです。

## 特徴

以下の4つのルールに基づいてパスワードの強度を判定します。

- 8文字以上であること
- 大文字と小文字の両方を含むこと
- 数字を1つ以上含むこと
- 特殊文字（`!@#$%^&*()_+-=[]{}|;:,.<>?/` のいずれか）を1つ以上含むこと

## インストール

特に追加のライブラリは必要ありません。Python 3.6以降で動作します。

## 使い方

```python
from password_checker import check_password_strength, Strength

result = check_password_strength("MyPassword1!")
print(result.strength)  # Strength.STRONG
print(result.strength.value)  # 強い

# 詳細な情報の取得
print(result.met_rules)    # 合格したルール一覧
print(result.failed_rules) # 不合格のルール一覧
```

## 開発とテスト

### テストの実行

```bash
pytest test_password_checker.py
```

### カバレッジの確認

```bash
pytest --cov=password_checker test_password_checker.py
```

### リンター

```bash
ruff check .
mypy .
```
