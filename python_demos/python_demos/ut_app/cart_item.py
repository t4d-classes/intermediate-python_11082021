class CartItem:

    def __init__(self, name: str, price: float, quantity: int = 0) -> None:

        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        return self.price * self.quantity

    def __repr__(self) -> str:

        quantity = str(self.quantity).ljust(2, ' ')
        name = self.name[:8].ljust(8, ' ')
        price = str(self.total_price()).rjust(5, ' ')

        return f"{quantity} x {name} {price}"
