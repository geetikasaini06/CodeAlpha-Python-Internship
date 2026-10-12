
# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 170
}

portfolio = {}
total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks and Prices:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input(
        "\nEnter stock name (or 'done' to finish): "
    ).upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    portfolio[stock_name] = (
        portfolio.get(stock_name, 0) + quantity
    )

print("\n========== YOUR PORTFOLIO ==========")

if not portfolio:
    print("No stocks were added.")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock}: {quantity} shares")
    print(f"Price per share: ${price}")
    print(f"Investment value: ${investment}")
    print("-----------------------------------")

print(f"Total Investment: ${total_investment}")
print("Thank you for using Stock Portfolio Tracker!")
