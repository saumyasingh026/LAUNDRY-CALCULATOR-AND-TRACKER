import datetime


class LaundryTracker:

    def __init__(self):
        # Default price per item type (in currency Indian rupees)
        self.rates = {
            "shirt": 15.00,
            "pants": 15.00,
            "jacket": 15.00,
            "bedsheet": 20.00,
            "towel": 10.00,
        }
        self.tracker = []

    def display_rates(self):
        print("\n--- Current Rate Card ---")
        for item, rate in self.rates.items():
            print(f"- {item.capitalize()}: ${rate:.2f}")

    def update_rate(self):
        item = input("\nEnter item name to update/add: ").strip().lower()
        try:
            rate = float(input(f"Enter new price for '{item}': $"))
            self.rates[item] = rate
            print(f"Updated: {item.capitalize()} rate set to ${rate:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numerical amount.")

    def add_laundry_item(self):
        self.display_rates()
        item = (
            input("\nEnter item type (or type a custom item): ").strip().lower()
        )

        if item not in self.rates:
            try:
                rate = float(input(f"Price for new item '{item}': $"))
                self.rates[item] = rate
            except ValueError:
                print("Invalid price. Item not added.")
                return

        try:
            quantity = int(input(f"How many '{item}' items? "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

            cost = quantity * self.rates[item]
            self.tracker.append(
                {
                    "item": item,
                    "quantity": quantity,
                    "unit_price": self.rates[item],
                    "total_cost": cost,
                    "time": datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M"
                    ),
                }
            )
            print(
                f"Added {quantity} x {item.capitalize()} = ${cost:.2f} to tracker."
            )
        except ValueError:
            print("Invalid input. Quantity must be a whole number.")

    def calculate_total(self):
        if not self.tracker:
            print("\nNo items currently logged in this session.")
            return

        print("\n" + "=" * 45)
        print("            LAUNDRY RECEIPT / SUMMARY         ")
        print("=" * 45)
        print(
            f"{'Item':<15} | {'Qty':<5} | {'Unit ($)':<8} | {'Total ($)':<8}"
        )
        print("-" * 45)

        grand_total = 0.0
        total_items = 0

        for entry in self.tracker:
            item_name = entry["item"].capitalize()
            qty = entry["quantity"]
            price = entry["unit_price"]
            cost = entry["total_cost"]

            grand_total += cost
            total_items += qty

            print(f"{item_name:<15} | {qty:<5} | {price:<8.2f} | {cost:<8.2f}")

        print("-" * 45)
        print(f"Total Pieces: {total_items}")
        print(f"Grand Total : ${grand_total:.2f}")
        print("=" * 45)


def main():
    app = LaundryTracker()

    while True:
        print("\n--- LAUNDRY TRACKER MENU ---")
        print("1. Add Laundry Items")
        print("2. View Current Rates")
        print("3. Update/Add Custom Rate")
        print("4. View Receipt & Total Amount")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            app.add_laundry_item()
        elif choice == "2":
            app.display_rates()
        elif choice == "3":
            app.update_rate()
        elif choice == "4":
            app.calculate_total()
        elif choice == "5":
            print("Exiting Laundry Tracker. Have a great day!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
