def main():
    print("=== Трекер расходов ===")
    print("1. Добавить расход")
    print("2. Показать все")
    print("3. Выход")

if __name__ == "__main__":
    main()
expenses = []

def sum_by_category():
    category = input("Категория: ")
    total = 0
    for e in expenses:
        if e["category"] == category:
            total += float(e["amount"])
    print(f"Итого по '{category}': {total}")

def add_expense():
    amount = input("Сумма: ")
    category = input("Категория: ")
    expenses.append({"amount": amount, "category": category})
    print("Добавлено!")

def show_expenses():
    if not expenses:
        print("Пока пусто")
        return
    for e in expenses:
        print(f"{e['amount']} — {e['category']}")

def main():
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
        elif choice == "4":
            sum_by_category()
            break
        else:
            print("Не понял, попробуй снова")

if __name__ == "__main__":
    main()
def sum_by_category():
    category = input("Категория: ")
    total = 0
    for e in expenses:
        if e["category"] == category:
            total += float(e["amount"])
    print(f"Итого по '{category}': {total}")
        