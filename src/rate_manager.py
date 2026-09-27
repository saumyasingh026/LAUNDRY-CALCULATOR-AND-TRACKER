import json
import os


class RateManager:

    def __init__(self, storage_path: str = "data/rates.json"):
        self.storage_path = storage_path
        self.rates = {
            "shirt": 2.50,
            "pants": 3.00,
            "jacket": 5.00,
            "bedsheet": 4.00,
            "towel": 1.50,
            "undergarment": 1.00,
        }
        self._load_rates()

    def _load_rates(self):
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, "r") as f:
                    self.rates.update(json.load(f))
            except json.JSONDecodeError:
                pass

    def save_rates(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, "w") as f:
            json.dump(self.rates, f, indent=4)

    def get_rate(self, item_name: str) -> float:
        return self.rates.get(item_name.lower())

    def update_rate(self, item_name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.rates[item_name.lower()] = price
        self.save_rates()
