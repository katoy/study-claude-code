# 家計簿アプリ

家計の収支を記録・集計するシンプルなCLIアプリケーションです。

## 特徴

- **収支の記録**: 日付、種別（収入/支出）、カテゴリ、金額、メモを記録
- **カテゴリ別集計**: カテゴリごとの合計金額を表示
- **月別レポート**: 月ごとの収入・支出・収支を表示
- **JSON保存**: トランザクションをJSONファイルに永続化

## インストール

依存ライブラリはありません。Python 3.9以降で動作します。

## 使い方

```bash
python3 cli.py
```

メニューから以下を選択できます：

1. **収支の記録**: 新しい取引を記録
   - 日付（デフォルト: 本日）
   - 種別（1: 収入、2: 支出）
   - カテゴリ
   - 金額
   - メモ（任意）

2. **カテゴリ別集計**: カテゴリごとの合計を表示

3. **月別レポート**: 月ごとの収支サマリーを表示

4. **終了**: アプリケーションを終了

## プロジェクト構成

```
ch08/
├── cli.py              # メインアプリケーション（メニュー、入出力）
├── models.py           # Transaction、TransactionType モデル
├── storage.py          # JSONStorage（永続化）
├── reports.py          # aggregate_by_category、aggregate_by_month（集計ロジック）
├── tests/
│   ├── test_cli.py     # CLI機能のテスト
│   └── test_reports.py # 集計機能のテスト
└── transactions.json   # トランザクションデータ（自動生成）
```

## 開発とテスト

### テストの実行

```bash
python3 -m pytest tests/
```

### カバレッジの確認

```bash
python3 -m pytest tests/ --cov=cli --cov=reports --cov-report=term-missing
```

### リンター・型チェック

```bash
ruff check .
mypy .
```

## 実装詳細

### モデル

**Transaction**: 一つの取引を表します
- date: 取引日（date）
- category: カテゴリ（str）
- amount: 金額（int）
- transaction_type: 種別（TransactionType.INCOME or .EXPENSE）
- note: メモ（str）

**TransactionType**: 取引種別（Enum）
- INCOME: 収入
- EXPENSE: 支出

### ストレージ

**JSONStorage**: `transactions.json` にトランザクションをシリアライズ/デシリアライズします

### 集計機能

- `aggregate_by_category()`: トランザクションをカテゴリごとに集計
- `aggregate_by_month()`: トランザクションを月ごとに集計

## テストカバレッジ

現在のカバレッジ: **100%**

- cli.py: 100%
- reports.py: 100%

全 23 テストケースが合格しています。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](./LICENSE) ファイルを参照してください。
