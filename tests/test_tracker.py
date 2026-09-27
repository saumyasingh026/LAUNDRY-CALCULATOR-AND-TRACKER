import unittest
from src.rate_manager import RateManager
from src.tracker import LaundryTracker


class TestLaundryTracker(unittest.TestCase):

    def setUp(self):
        self.rate_manager = RateManager(storage_path="data/test_rates.json")
        self.tracker = LaundryTracker(self.rate_manager)

    def test_add_item(self):
        item = self.tracker.add_item("shirt", 3)
        self.assertEqual(item.quantity, 3)
        self.assertEqual(item.total_cost, 7.50)

    def test_total_calculation(self):
        self.tracker.add_item("shirt", 2)  # 2 * 2.50 = 5.00
        self.tracker.add_item("pants", 1)  # 1 * 3.00 = 3.00
        self.assertEqual(self.tracker.calculate_grand_total(), 8.00)
        self.assertEqual(self.tracker.calculate_total_items(), 3)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.tracker.add_item("shirt", 0)

    def tearDown(self):
        import os

        if os.path.exists("data/test_rates.json"):
            os.remove("data/test_rates.json")


if __name__ == "__main__":
    unittest.main()
