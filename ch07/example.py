from password_checker import check_password_strength

def main() -> None:
    passwords = [
        "abc",
        "Abcdefgh",
        "Abcdef1!",
        "P@ssw0rd2024",
        "My_New_Pwd+1",
    ]

    print("--- パスワード強度チェック ---")
    for pwd in passwords:
        result = check_password_strength(pwd)
        print(f"Password: {pwd:<15} -> Strength: {result.strength.value}")
        if result.failed_rules:
            print(f"  [不足している条件]: {', '.join(result.failed_rules)}")
        else:
            print("  [全ての条件をクリアしています]")

    print("\n--- エラーハンドリングの例 ---")
    try:
        check_password_strength(None)
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
