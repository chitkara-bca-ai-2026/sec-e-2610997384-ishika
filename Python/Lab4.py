
product_name = input("Enter Product Name : ")
price = float(input("Enter Price : "))
quantity = int(input("Enter Quantity : "))

total_price = price * quantity
amount_str = str(total_price)

print("\nTYPE CASTING SUMMARY")
print(f"product_name {product_name} {type(product_name)}")
print(f"price {price} {type(price)}")
print(f"quantity {quantity} {type(quantity)}")
print(f"total_price {total_price} {type(total_price)}")
print(f"amount_str {amount_str} {type(amount_str)}")

print("\nTAX INVOICE")
print(f"Product Name : {product_name}")
print(f"Price per Unit : Rs. {price}")
print(f"Quantity : {quantity}")
print(f"Invoice Total : Rs. {amount_str}")