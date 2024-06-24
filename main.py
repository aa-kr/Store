class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"товар{item_name} добавлен в магазин {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"товар {item_name} удален из магазина {self.name}")
        else:
            print(f"товар {item_name} не найден в магазине {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"цена товара {item_name} обновлена в магазине {self.name}")
        else:
            print(f"товар {item_name} не найден в магазине {self.name}")


store1 = Store("Магазин1", "ул. Ленина, д. 10")
store2 = Store("Магазин2", "ул. Пушкина, д. 5")
store3 = Store("Магазин3", "ул. Строителей, д. 15")

store1.add_item("Хлеб", 50)
store1.add_item("Молоко", 80)
store1.add_item("Яблоки", 30)

store1.remove_item("Хлеб")

print(store1.get_price("Молоко"))

store1.update_price("Яблоки", 90)


