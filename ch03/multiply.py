import sys

def multiply(a: float, b: float) -> float:
    return a * b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使い方: python multiply.py <数字1> <数字2>")
        sys.exit(1)
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("エラー: 数値を入力してください")
        sys.exit(1)
    print(f"{a} × {b} = {multiply(a, b)}")
