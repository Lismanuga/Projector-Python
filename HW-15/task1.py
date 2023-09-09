class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author) -> None:
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        return f'{self.name} - {self.price} - {self.quantity} - {self.author}'


book = Book('Harry Poter', 300, 10000, 'J.Roling')
print(book.read())
