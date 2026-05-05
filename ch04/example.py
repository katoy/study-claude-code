from password_checker import check_password_strength

def main() -> None:
    passwords = [
        "abc",
        "Abcdefgh",
        "Abcdef1!",
    ]

    for pwd in passwords:
        strength = check_password_strength(pwd)
        print(f"Password: {pwd:<10} -> Strength: {strength}")

if __name__ == "__main__":
    main()
