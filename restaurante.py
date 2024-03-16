class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total_price(self, quantity):
        return self.price * quantity

class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

class Appetizer(MenuItem):
    pass

class MainCourse(MenuItem):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def calculate_total_bill(self):
        total_bill = 0
        itemized_bill = []
        for item, quantity in self.items.items():
            item_price = item.calculate_total_price(quantity)
            total_bill += item_price
            itemized_bill.append((item.name, item_price, quantity))
        return total_bill, itemized_bill

menu = {
    "Coke": Beverage("Coke", 2.500, "Large"),
    "Orange Juice": Beverage("Orange Juice", 1.500, "Medium"),
    "Caesar Salad": Appetizer("Caesar Salad", 8.000),
    "Chicken Wings": Appetizer("Chicken Wings", 12.000),
    "Spaghetti Bolognese": MainCourse("Spaghetti Bolognese", 15.000, ["Spaghetti", "Tomato Sauce", "Ground Beef"]),
    "Grilled Salmon": MainCourse("Grilled Salmon", 23.000, ["Salmon", "Lemon", "Herbs"]),
    "French Fries": MenuItem("French Fries", 7.500),
    "Cheeseburger": MenuItem("Cheeseburger", 15.000),
    "Cheesecake": MenuItem("Cheesecake", 9.500),
    "Ice Cream Sundae": MenuItem("Ice Cream Sundae", 3.500)
}

if __name__ == "__main__":
    order = Order()
    order.add_item(menu["Coke"], 2)
    order.add_item(menu["Caesar Salad"])
    order.add_item(menu["Grilled Salmon"])
    order.add_item(menu["Ice Cream Sundae"])

    total_bill, itemized_bill = order.calculate_total_bill()
    print("Itemized Bill:")
    for item, price, quantity in itemized_bill:
        print(f"{item}: {price:.3f} (Quantity: {quantity})")
    print("Total Bill: {:.3f}".format(total_bill))
