# ch03 プロジェクト構築プロンプト

## プロジェクト概要

2 つの数値を受け取り、掛け算の結果を出力する Python スクリプト。

## 必須依存関係

- [uv](https://docs.astral.sh/uv/) — Python パッケージマネージャー

## ファイル構成と実装内容

### 1. `pyproject.toml` — プロジェクト設定

```toml
[project]
name = "study-claude-code"
version = "0.1.0"
requires-python = ">=3.11"

[dependency-groups]
dev = [
  "mypy>=1.0",
  "ruff>=0.4",
  "pytest>=8.0",
  "pytest-cov>=5.0",
]
```

**特徴:**
- Python 3.11 以上が必須
- mypy （型チェック）、ruff （リンター）、pytest （テストフレームワーク）、pytest-cov （カバレッジ計測）をインストール

### 2. `multiply.py` — メインモジュール

**要件:**
- `multiply(a: float, b: float) -> float` 関数
  - 2 つの数値の積を float で返す
  - docstring: 「2 つの数値の積を float で返す。」

- `parse_args(argv: Optional[List[str]] = None) -> Tuple[float, float]` 関数
  - argv を受け取り、プログラム名の後に正確に 2 つの数値引数を期待
  - 無効な入力の場合は ValueError を発生
  - docstring: 「引数を解析および検証する。argv を受け取ります (インデックス 0 にはプログラム名を含む)。プログラム名の後に正確に 2 つの数値引数を期待します。無効な入力の場合は ValueError を発生させます。」

- `main(argv: Optional[List[str]] = None) -> None` 関数
  - コマンドラインのエントリーポイント
  - 成功時に結果を出力 (例: `3.0 × 4.0 = 12.0`)
  - エラー時にエラーメッセージを表示し、コード 1 で終了
  - docstring: 「コマンドラインのエントリーポイント。同じ動作を保ちます: 成功時に結果を出力し、エラー時にコード 1 で終了して既存のテストと CLI 使用法との互換性を保ちます。」

**コメント規約:**
- 全てのコメント、docstring は日本語で記述
- 英数字と全角文字の間に半角スペースを挿入
  - 例：`# multiply(a, b) に 2 つの数値の積を float で返す`

**型ヒント:**
- `from __future__ import annotations` をインポート
- `List`, `Optional`, `Tuple` を `typing` からインポート
- 全ての関数に型ヒントを付与

**その他:**
- `if __name__ == "__main__": main()` ブロックを含める

### 3. `conftest.py` — pytest 設定

```python
import sys
import pytest

@pytest.fixture(autouse=True)
def reset_modules():
    yield
    if "multiply" in sys.modules:
        del sys.modules["multiply"]
```

**要件:**
- `reset_modules` フィクスチャーを定義 (テスト間でモジュール状態をリセット)
- `autouse=True` で全テストに自動適用

### 4. `tests/test_multiply.py` — テストスイート

**テストケース:**

1. `test_multiply_integers()` — `multiply(3, 4) == 12.0` を検証
2. `test_multiply_floats()` — `multiply(2.5, 3.0) == 7.5` を検証
3. `test_multiply_negative()` — `multiply(-2, 5) == -10.0` を検証
4. `test_multiply_zero()` — `multiply(0, 99) == 0.0` を検証
5. `test_main_normal(capsys)` — CLI で `multiply.py 3 4` を実行し、`3.0 × 4.0 = 12.0` を出力
6. `test_main_no_args(capsys)` — 引数がない場合、exit code 1 で終了
7. `test_main_invalid_args(capsys)` — 非数値引数の場合、exit code 1 で終了
8. `test_main_entry_point(monkeypatch, capsys)` — `__main__` ブロックの実行を検証

**要件:**
- `sys.argv` をモック/モンキーパッチして CLI 挙動をテスト
- `capsys` で stdout を検証
- `pytest.raises(SystemExit)` で終了コードを検証

### 5. `README.md` — ドキュメント

**内容:**
- プロジェクト概要
- 必要条件（uv）
- セットアップ手順（`uv sync`）
- git フック設定（`git config core.hooksPath .githooks` と chmod）
- 使い方（例：`uv run python multiply.py 3 4`）
- 開発ツール（`uv run ruff check`, `uv run mypy .`）

### 6. `.githooks/pre-push` — Git フック（初回セットアップが必要）

**機能:**
- push 前にカバレッジ 100% をチェック
- .githooks フォルダは初回セットアップで `chmod +x` を実行

## セットアップ手順

```bash
# 1. プロジェクトの依存関係をインストール
uv sync

# 2. git フック設定（初回のみ）
git config core.hooksPath .githooks
chmod +x .githooks/pre-push
```

## コード品質基準

1. **型チェック**: `uv run mypy .` で エラーなし
2. **リンター**: `uv run ruff check` で エラーなし
3. **テストカバレッジ**: 100% (全ブランチをカバー)
4. **コメント**: 全て日本語、英数字と全角文字間に半角スペース

## 実行例

```bash
$ uv run python multiply.py 3 4
3.0 × 4.0 = 12.0

$ uv run python multiply.py 2.5 3
2.5 × 3.0 = 7.5
```

## テスト実行

```bash
# 全テストの実行
uv run pytest

# カバレッジ付きで実行
uv run pytest --cov=. --cov-report=term-missing
```
