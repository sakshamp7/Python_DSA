prices = list(map(int, input("Enter the stock price:").split()))
min_price = float("inf")
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    profit = price - min_price

    if profit > max_profit:
        max_profit = profit

print("Maximum profit:", max_profit)
