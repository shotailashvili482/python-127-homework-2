#Bonus: price with VAT

input_price = float(input("Enter a price: "))
VAT_RATE = 0.18

price = round(input_price * (1 + VAT_RATE), 2)

print(f"Total with VAT: {price}")