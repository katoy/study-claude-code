from datetime import date
from models import Transaction, TransactionType
from storage import JSONStorage
from reports import aggregate_by_category, aggregate_by_month

def get_input(prompt: str, default: str = "") -> str:
    full_prompt = f"{prompt} [{default}]: " if default else f"{prompt}: "
    user_input = input(full_prompt).strip()
    return user_input if user_input else default

def record_transaction(storage: JSONStorage) -> None:
    print("\n--- 収支の記録 ---")
    
    # 日付の入力
    date_str = get_input("日付 (YYYY-MM-DD)", date.today().isoformat())
    try:
        txn_date = date.fromisoformat(date_str)
    except ValueError:
        print("エラー: 日付の形式が正しくありません。")
        return

    # 種別の入力
    type_input = get_input("種別 (1: 収入, 2: 支出)", "2")
    if type_input == "1":
        txn_type = TransactionType.INCOME
    elif type_input == "2":
        txn_type = TransactionType.EXPENSE
    else:
        print("エラー: 1 または 2 を入力してください。")
        return

    # カテゴリの入力
    category = get_input("カテゴリ")
    if not category:
        print("エラー: カテゴリは必須です。")
        return

    # 金額の入力
    while True:
        amount_str = get_input("金額")
        try:
            amount = int(amount_str)
            if amount < 0:
                print("エラー: 金額に負の値を入力することはできません。")
                continue
            break
        except ValueError:
            print("エラー: 金額は数値で入力してください。")
            continue

    # メモの入力
    note = get_input("メモ (任意)")

    # 保存
    new_txn = Transaction(
        date=txn_date,
        category=category,
        amount=amount,
        transaction_type=txn_type,
        note=note
    )
    
    transactions = storage.load_transactions()
    transactions.append(new_txn)
    storage.save_transactions(transactions)
    
    print(f"\n記録しました: {txn_type.value} - {category}: {amount}円")

def _load_transactions_or_exit(storage: JSONStorage) -> list[Transaction] | None:
    transactions = storage.load_transactions()
    if not transactions:
        print("データがありません。")
        return None
    return transactions

def show_category_report(storage: JSONStorage) -> None:
    print("\n--- カテゴリ別集計 ---")
    transactions = _load_transactions_or_exit(storage)
    if not transactions:
        return

    report = aggregate_by_category(transactions)

    print("\n[支出]")
    if report[TransactionType.EXPENSE]:
        for cat, total in report[TransactionType.EXPENSE].items():
            print(f"  {cat}: {total}円")
    else:
        print("  記録なし")

    print("\n[収入]")
    if report[TransactionType.INCOME]:
        for cat, total in report[TransactionType.INCOME].items():
            print(f"  {cat}: {total}円")
    else:
        print("  記録なし")

def show_monthly_report(storage: JSONStorage) -> None:
    print("\n--- 月別レポート ---")
    transactions = _load_transactions_or_exit(storage)
    if not transactions:
        return

    report = aggregate_by_month(transactions)

    for month in sorted(report.keys()):
        inc = report[month][TransactionType.INCOME]
        exp = report[month][TransactionType.EXPENSE]
        diff = inc - exp
        print(f"\n{month}:")
        print(f"  収入: {inc}円")
        print(f"  支出: {exp}円")
        print(f"  収支: {diff}円")

def main() -> None:
    storage = JSONStorage("transactions.json")

    while True:
        print("\n=== 家計簿アプリ ===")
        print("1: 収支の記録")
        print("2: カテゴリ別集計")
        print("3: 月別レポート")
        print("4: 終了")

        choice_str = get_input("選択してください", "1")
        try:
            choice = int(choice_str)
        except ValueError:
            print("エラー: 1〜4の数値を入力してください。")
            continue

        if choice == 1:
            record_transaction(storage)
        elif choice == 2:
            show_category_report(storage)
        elif choice == 3:
            show_monthly_report(storage)
        elif choice == 4:
            print("プログラムを終了します。")
            break
        else:
            print("エラー: 1〜4の数値を入力してください。")

if __name__ == "__main__":
    main()
