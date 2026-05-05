# API Reference

## `password_checker.py`

### `check_password_strength(password: str) -> PasswordResult`

パスワードの強度を評価し、詳細情報を含む `PasswordResult` オブジェクトを返します。

#### 引数
- `password` (str): チェック対象のパスワード文字列。

#### 戻り値
- `PasswordResult`: 以下の属性を持つオブジェクト。
    - `strength` (Strength): 強度（Enum）。
    - `met_rules` (List[str]): 満たしているルールのリスト。
    - `failed_rules` (List[str]): 満たしていないルールのリスト。

### `Strength` (Enum)
- `WEAK`: `"弱い"` (ルール 0〜1 個)
- `MEDIUM`: `"普通"` (ルール 2〜3 個)
- `STRONG`: `"強い"` (ルール 4 個)

### `PasswordResult` (dataclass)
判定結果と詳細なフィードバックを保持します。
文字列として評価した場合は `strength.value` を返します。

#### 強度判定ルール
1. **長さ**: 8文字以上
2. **文字種**: 大文字と小文字の両方を含む
3. **数字**: 1つ以上の数字を含む
4. **特殊文字**: `!@#$%^&*()_+-=[]{}|;:,.<>?/` のいずれかを含む

#### 例外
- `TypeError`: `password` が文字列でない場合に発生します。
