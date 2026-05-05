# API Documentation

## `find_range(numbers)`

リスト内の最大値と最小値の差を計算します。

### 引数 (Arguments)

| 名前 | 型 | 説明 |
| :--- | :--- | :--- |
| `numbers` | `list[int\|float]` | 数値（整数または浮動小数点数）のリスト |

### 戻り値 (Returns)

| 型 | 説明 |
| :--- | :--- |
| `int\|float` | リスト内の最大値と最小値の差 |

### 例外 (Raises)

| 例外名 | 条件 |
| :--- | :--- |
| `ValueError` | `numbers` が空のリストの場合 |

### 使用例 (Usage Examples)

```python
from find_range import find_range

# 通常のリスト
print(find_range([1, 5, 3, 9, 2]))  # 出力: 8 (9 - 1)

# 負の数を含む
print(find_range([-5, 0, 10, 3]))  # 出力: 15 (10 - (-5))

# 1つの要素だけのリスト
print(find_range([7]))  # 出力: 0 (7 - 7)

# 空のリスト（エラー）
try:
    find_range([])
except ValueError as e:
    print(e)  # 出力: 空のリストは渡せません
```
