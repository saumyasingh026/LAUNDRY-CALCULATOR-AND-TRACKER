from src.rate_manager import RateManager
from src.tracker import LaundryTracker


def display_receipt(tracker: LaundryTracker):
    if not tracker.items:
        print("\n[!] No items added to the tracker yet.")
        return

    print("\n" + "=" * 50)
    print("           LAUNDRY RECEIPT & SUMMARY           ")
    print("=" * 50)
    print(
        f"{'Item':<15} | {'Qty':<5} | {'Unit ($)':<8} | {'Total ($)':<8}"
    )
    print("-" * 50)

    for item in tracker.items:
        print(
            f"{item.name.capitalize():<15} | {item.quantity:<5} | "
            f"{item.unit_price:<8.2f} | {item.total_cost:<8.2f}"
        )

    print("-" * 50)
    print(f"Total Pieces : {tracker.calculate_total_items()}")
    print(f"Grand Total  : ${tracker.calculate_grand_total():.2f}")
    print("=" * 50)


def main():
    rate_manager = RateManager()
    tracker = LaundryTracker(rate_manager)

    while True:
        print("\n--- LAUNDRY TRACKER MENU ---")
        print("1. View Rate Card")
        print("2. Add Laundry Item")
        print("3. Update/Add Rate")
        print("4. View Receipt & Calculate Total")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            print("\n--- Current Rates ---")
            for item, rate in rate_manager.rates.items():
                print(f"- {item.capitalize()}: ${rate:.2f}")

        elif choice == "2":
            name = input("Enter item name: ").strip()
            rate = rate_manager.get_rate(name)

            if rate is None:
                try:
                    new_rate = float(
                        input(
                            f"Item '{name}' not found. Enter unit price: $"
                        )
                    )
                    rate_manager.update_rate(name, new_rate)
                except ValueError:
                    print("[!] Invalid price. Item creation cancelled.")
                    continue

            try:
                qty = int(input(f"Enter quantity for '{name}': "))
                tracker.add_item(name, qty)
                print(f"[✓] Added {qty} x {name.capitalize()}")
            except ValueError as e:
                print(f"[!] Input Error: {e}")

        elif choice == "3":
            name = input("Enter item name: ").strip()
            try:
                price = float(input(f"Enter new price for '{name}': $"))
                rate_manager.update_rate(name, price)
                print(f"[✓] Rate updated for {name.capitalize()}.")
            except ValueError as e:
                print(f"[!] Error: {e}")

        elif choice == "4":
            display_receipt(tracker)

        elif choice == "5":
            print("Thank you for using Laundry Tracker. Goodbye!")
            break

        else:
            print("[!] Invalid selection. Please choose 1-5.")


if __name__ == "__main__":
    main()
