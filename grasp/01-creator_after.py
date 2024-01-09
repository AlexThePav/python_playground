from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ProductDescription:
    price: int
    description: str


@dataclass
class SaleLineItem:
    product: ProductDescription
    quantity: int


@dataclass
class Sale:
    items: list[SaleLineItem] = field(default_factory=list)
    time: datetime = field(default_factory=datetime.now)

    def add_line_item(self, product: ProductDescription, quantity: int):
        self.items.append(SaleLineItem(product, quantity))


def main() -> None:
    headset = ProductDescription(price=5000, description="Gaming headset")
    keyboard = ProductDescription(price=7500, description="Mechanical gaming keyboard")

    sale = Sale()
    sale.add_line_item(headset, 2)
    sale.add_line_item(keyboard, 3)

    print(sale)


if __name__ == "__main__":
    main()
