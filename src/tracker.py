from typing import List
from src.models import LaundryItem
from src.rate_manager import RateManager


class LaundryTracker:

    def __init__(self, rate_manager: RateManager):
        self.rate_manager = rate_manager
        self.items: List[LaundryItem] = []

    def add_item(self, item_name: str, quantity: int) -> LaundryItem:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        rate = self.rate_manager.get_rate(item_name)
        if rate is None:
            raise KeyError(f"No rate defined for item '{item_name}'.")

        item = LaundryItem(
            name=item_name.lower(), quantity=quantity, unit_price=rate
        )
        self.items.append(item)
        return item

    def calculate_grand_total(self) -> float:
        return sum(item.total_cost for item in self.items)

    def calculate_total_items(self) -> int:
        return sum(item.quantity for item in self.items)

    def clear_tracker(self):
        self.items.clear()
