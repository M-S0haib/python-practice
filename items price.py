print("PLEASE ENTER THE BELOW DETAILS")

print("YOUR NAME")
name = input()

print("YOUR CELL NO:")
cell_no = int(input())

print("HOW MANY ITEMS HAVE YOU BOUGHT?")
items_bought = int(input())  # Convert input to integer

print("ENTER THE PRICE OF EACH ITEM")

total_price = 0  # Initialize total price variable

# Loop to get price of each item
for i in range(items_bought):
    item_price = float(input(f"Enter the price of item {i + 1}: "))  # Convert input to float
    total_price += item_price  # Add item price to total price

print("Total price for all items:", total_price)

tax = (total_price * 5) / 100

with_tax_price = tax + total_price

if (with_tax_price > 500):
    discount = (with_tax_price * 15) / 100

    actual_amount = with_tax_price - discount
    print("YOU GOT A DISCOUNT OF 15 % TOTAL AMOUNT IS" , actual_amount)
    
    
