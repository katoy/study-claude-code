def find_range(numbers):
    """
    リスト内の最大値と最小値の差を計算する関数

    Args:
        numbers: 数値のリスト

    Returns:
        最大値と最小値の差（int または float）

    Raises:
        ValueError: 空のリストが渡された場合
    """
    if not numbers:
        raise ValueError("空のリストは渡せません")

    return max(numbers) - min(numbers)
