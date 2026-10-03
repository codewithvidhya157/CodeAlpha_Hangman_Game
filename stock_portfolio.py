
# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

print("================================")
print("    STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable stocks:")
for stock in stock_prices:
    print(stock, "- $", stock_prices[stock])

# Number of stocks the user wants to enter
number_of_stocks = int(input("\nHow many stocks do you want to add? "))

for i in range(number_of_stocks):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Investment for", stock_name, ":", "$", investment)

    else:
        print("Stock not available.")

print("\n================================")
print("Total Investment: $", total_investment)
print("================================")