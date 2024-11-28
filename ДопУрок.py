import sqlite3


conn = sqlite3.connect("db/shop.db")
cursor = conn.cursor()
conn.commit()


cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS store (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(250) NOT NULL,
    category_code VARCHAR(2),
    unit_price FLOAT NOT NULL,
    stock_quantity INTEGER NOT NULL,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories(code),
    FOREIGN KEY (store_id) REFERENCES store(store_id)
)
""")

conn.commit()
conn.close()


def get_stores():
    with sqlite3.connect("shop.db") as conn:
        return conn.execute("SELECT store_id, title FROM store").fetchall()


def get_products_by_store(store_id):
    with sqlite3.connect("shop.db") as conn:
        return conn.execute("""
            SELECT p.title, c.title, p.unit_price, p.stock_quantity
            FROM products p
            LEFT JOIN categories c ON p.category_code = c.code
            WHERE p.store_id = ?
        """, (store_id,)).fetchall()


def main():
    while True:
        print(
            "\nВы можете отобразить список продуктов по выбранному id магазина из "
            "перечня магазинов ниже, для выхода из программы введите цифру 0:")

        stores = get_stores()
        if not stores:
            print("Список магазинов пуст. Сначала добавьте магазины в базу данных.")
            break

        for store_id, title in stores:
            print(f"{store_id}. {title}")

        user_input = input("Введите ID магазина или 0 для выхода: ")

        if user_input == '0':
            print("Выход из программы.")
            break

        if not user_input.isdigit():
            print("Некорректный ввод. Введите числовое значение.")
            continue

        store_id = int(user_input)
        if not any(store[0] == store_id for store in stores):
            print("Магазин с таким ID не найден. Попробуйте снова.")
            continue

        products = get_products_by_store(store_id)
        if products:
            print(f"\nПродукты в магазине ID {store_id}:")
            for title, category, price, quantity in products:
                print(
                    f"Название продукта: {title}\nКатегория: {category}\nЦена: "
                    f"{price}\nКоличество на складе: {quantity}\n")
        else:
                print("Вы ошиблись")


if __name__ == "__main__":
    main()
