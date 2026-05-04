# ch03 - 掛け算スクリプト

## Table of Contents

- [概要](#概要)
- [必要条件](#必要条件)
- [セットアップ](#セットアップ)
- [使い方](#使い方)
- [開発ツール](#開発ツール)

## 概要

2つの数値を受け取り、掛け算の結果を出力する Python スクリプト。

## 必要条件

- [uv](https://docs.astral.sh/uv/) — Python パッケージマネージャー

## セットアップ

```bash
uv sync
```

## 使い方

```bash
uv run python multiply.py <数字1> <数字2>
```

**実行例：**

```bash
$ uv run python multiply.py 3 4
3.0 × 4.0 = 12.0

$ uv run python multiply.py 2.5 3
2.5 × 3.0 = 7.5
```

## 開発ツール

```bash
# コード品質チェック
uv run ruff check

# 型チェック
uv run mypy .
```
