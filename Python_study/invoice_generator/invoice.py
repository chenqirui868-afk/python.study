product = input("Product name: ")
price = float(input("Unit price: "))
quantity = int(input("Quantity: "))
subtotal = price * quantity
gst_rate = 0.15
GST = subtotal * gst_rate
total = GST + subtotal

print("==============================")
print("      SALES INVOICE")
print("==============================")
print(f"Product: {product}")
print(f"Unit price: ${price}")
print(f"Quantity: {quantity}")
print(f"GST: ${gst_rate}")
print(f"Total: ${total}")
