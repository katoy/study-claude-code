"""シンプルな乗算モジュールと小さい CLI を提供します。

このモジュールは以下を提供します:
- multiply(a, b): 2 つの数値の積を float で返す
- parse_args(argv): CLI 引数を解析および検証する
- main(argv=None): エントリーポイント (既存のテストとの互換性を保つ)
"""

from __future__ import annotations

from typing import List, Optional, Tuple
import sys


def multiply(a: float, b: float) -> float:
    """2 つの数値の積を float で返す。"""
    return a * b


def parse_args(argv: Optional[List[str]] = None) -> Tuple[float, float]:
    """引数を解析および検証する。

    argv を受け取ります (インデックス 0 にはプログラム名を含む)。プログラム名の後に正確に 2 つの数値
    引数を期待します。無効な入力の場合は ValueError を発生させます。
    """
    if argv is None:
        argv = sys.argv  # pragma: no cover

    if len(argv) != 3:
        raise ValueError("Expected two numeric arguments")

    try:
        a = float(argv[1])
        b = float(argv[2])
    except (ValueError, TypeError):
        raise ValueError("Arguments must be numbers")

    return a, b


def main(argv: Optional[List[str]] = None) -> None:
    """コマンドラインのエントリーポイント。

    同じ動作を保ちます: 成功時に結果を出力し、エラー時にコード 1 で終了して既存のテストと
    CLI 使用法との互換性を保ちます。
    """
    if argv is None:
        argv = sys.argv

    try:
        a, b = parse_args(argv)
    except ValueError:
        print("エラー: 引数を2つの数値で指定してください")
        sys.exit(1)

    print(f"{a} × {b} = {multiply(a, b)}")


if __name__ == "__main__":  # pragma: no cover
    main()
