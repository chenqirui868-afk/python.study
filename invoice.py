product = input("Product name: ")
price = float(input("Unit price: "))
quantity = int(input("Quantity: "))
discount_rate = float(input("Discount rate: "))
discount_rate = discount_rate / 100
subtotal = price * quantity
discount = subtotal * discount_rate
after_discount = subtotal - discount
gst_rate = 0.15
GST = after_discount * gst_rate
total = GST + after_discount

print("==============================")
print("      SALES INVOICE")
print("==============================")
print(f"Product: {product}")
print(f"Unit price: ${price}")
print(f"Quantity: {quantity}")
print(f"Discount rate: ${discount_rate}")
print(f"Discount amount: ${discount}")
print(f"after_discount: ${after_discount}")
print(f"GST: ${GST}")
print(f"Total: ${total}")
