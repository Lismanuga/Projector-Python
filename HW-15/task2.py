class Restaurant:
    def __init__(self, name, cuisine, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu: dict, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish, quantity):
        if dish not in self.menu.keys():
            return 'Dish not available'
        if quantity > self.menu[dish]['quantity']:
            return 'Requested quantity not available'
        total_cost = quantity * self.menu[dish]['price']
        self.menu[dish]['quantity'] -= quantity
        return total_cost


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # Output: 25
print(mc.order('burger', 15))  # Output: Requested quantity not available
print(mc.order('soup', 5))  # Output: Dish not available
