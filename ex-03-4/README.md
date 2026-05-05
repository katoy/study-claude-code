# ex-03-4: Find Range Utility

数値リスト内の最大値と最小値の差を計算するシンプルな Python ユーティリティです。

## プロジェクト概要

このプロジェクトは、提供された数値リストから「範囲」（最大値 - 最小値）を計算する `find_range` 関数を提供します。
教育目的や、シンプルな数値計算が必要な小規模プロジェクトに適しています。

## 必要な環境

- Python 3.6 以上
- pytest (テストを実行する場合)

## インストール手順

1. このリポジトリをクローンするか、ファイルをダウンロードします。
   ```bash
   git clone https://github.com/katoy/study-claude-code.git
   cd study-claude-code/ex-03-4
   ```

2. (任意) テスト用の依存関係をインストールします。
   ```bash
   pip install pytest
   ```

## 使い方

### コード例

`find_range` 関数をインポートして使用します。

```python
from find_range import find_range

# 通常のリスト
numbers = [1, 5, 3, 9, 2]
result = find_range(numbers)
print(f"Range: {result}")  # Output: Range: 8

# 負の数を含むリスト
numbers = [-5, 0, 10, 3]
result = find_range(numbers)
print(f"Range: {result}")  # Output: Range: 15
```

### 実行例スクリプトの実行

同梱されている `example.py` を実行することで、動作を確認できます。

```bash
python example.py
```

### テストの実行

pytest を使用してテストを実行できます。

```bash
pytest test_find_range.py
```

## ライセンス

MIT License
