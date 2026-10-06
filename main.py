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
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['amount']} — {e['category']}")

def sum_by_category():
    category = input("Категория: ")
    total = 0
    for e in expenses:
        if e["category"] == category:
            total += float(e["amount"])
    print(f"Итого по '{category}': {total}")

def delete_expense():
    if not expenses:
        print("Нечего удалять")
        return
    show_expenses()
    try:
        index = int(input("Номер для удаления: ")) - 1
    except ValueError:
        print("Нужно ввести число")
        return
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save()
        print("Удалено")
    else:
        print("Нет такого номера")

def main():
    load()
    while True:
        print("\n=== Трекер расходов ===")
        print("1. Добавить расход")
        print("2. Показать все")
        print("3. Выход")
        print("4. Сумма по категории")
        print("5. Удалить расход")
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
        elif choice == "5":
            delete_expense()
        else:
            print("Не понял, попробуй снова")

if __name__ == "__main__":
    main()