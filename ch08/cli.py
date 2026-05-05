from datetime import date
from models import Transaction, TransactionType
from storage import JSONStorage

def get_input(prompt: str, default: str = "") -> str:
    full_prompt = f"{prompt} [{default}]: " if default else f"{prompt}: "
    user_input = input(full_prompt).strip()
    return user_input if user_input else default

def record_transaction(storage: JSONStorage):
    print("--- 収支の記録 ---")
    
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

if __name__ == "__main__":
    storage = JSONStorage("transactions.json")
    record_transaction(storage)
