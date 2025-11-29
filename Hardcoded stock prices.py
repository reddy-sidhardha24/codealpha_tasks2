# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

def main():
    portfolio = {}
    total_value = 0

    print("=== Simple Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    print("Type 'done' when finished.\n")

    while True:
        stock = input("Enter stock symbol: ").upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found. Try again.")
            continue

        qty = input(f"Enter quantity for {stock}: ")

        if not qty.isdigit():
            print("Please enter a valid number.")
            continue

        qty = int(qty)
        portfolio[stock] = portfolio.get(stock, 0) + qty

    # Calculate total investment
    print("\nCalculating investment...\n")

    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * qty
        total_value += value
        print(f"{stock}: {qty} shares x ${price} = ${value}")

    print("\nTotal Portfolio Value =", total_value)

    # Save results?
    save = input("\nDo you want to save this to a file? (yes/no): ").lower()

    if save == "yes":
        file_type = input("Save as .txt or .csv?: ").lower()

        if file_type == "txt":
            with open("portfolio.txt", "w") as f:
                f.write("Stock Portfolio Summary\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock}: {qty} shares = ${STOCK_PRICES[stock] * qty}\n")
                f.write(f"Total Value: ${total_value}\n")
            print("Saved as portfolio.txt")

        elif file_type == "csv":
            with open("portfolio.csv", "w") as f:
                f.write("Stock,Quantity,Price,Value\n")
                for stock, qty in portfolio.items():
                    price = STOCK_PRICES[stock]
                    value = qty * price
                    f.write(f"{stock},{qty},{price},{value}\n")
            print("Saved as portfolio.csv")

        else:
            print("Invalid file type. Skipping save.")

    print("\nThank you for using the tracker!")

if __name__ == "__main__":
    main()
