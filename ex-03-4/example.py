from find_range import find_range


if __name__ == "__main__":
    # テストケース 1: 通常のリスト
    test1 = [1, 5, 3, 9, 2]
    print(f"テスト 1: {test1}")
    print(f"結果: {find_range(test1)}")
    print()

    # テストケース 2: 負の数を含む
    test2 = [-5, 0, 10, 3]
    print(f"テスト 2: {test2}")
    print(f"結果: {find_range(test2)}")
    print()

    # テストケース 3: 1 つの要素だけのリスト
    test3 = [7]
    print(f"テスト 3: {test3}")
    print(f"結果: {find_range(test3)}")
    print()

    # テストケース 4: 空のリスト（エラーハンドリング）
    try:
        test4 = []
        print(f"テスト 4: {test4}")
        print(f"結果: {find_range(test4)}")
    except ValueError as e:
        print(f"エラーが発生しました: {e}")
