import json

FILE = "expenses.json"
expenses = []

def load():
    global expenses
    try:
        with open(FILE, "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

def save():
    with open(FILE, "w") as f:
        json.dump(expenses, f)

def add_expense():
    amount = input("Сумма: ")
    category = input("Категория: ")
    expenses.append({"amount": amount, "category": category})
    save()
    print("Добавлено!")

def show_expenses():
    if not expenses:
        print("Пока пусто")
        return
    for e in expenses:
        print(f"{e['amount']} — {e['category']}")

def sum_by_category():
    category = input("Категория: ")
    total = 0
    for e in expenses:
        if e["category"] == category:
            total += float(e["amount"])
    print(f"Итого по '{category}': {total}")

def main():
    load()
    while True:
        print("\n=== Трекер расходов ===")
        print("1. Добавить расход")
        print("2. Показать все")
        print("3. Выход")
        print("4. Сумма по категории")
        choice = input("Выбор: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            print("Пока!")
            break
        elif choice == "4":
            sum_by_category()
        else:
            print("Не понял, попробуй снова")

if __name__ == "__main__":
    main()