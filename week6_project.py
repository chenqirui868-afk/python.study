product = input("Product name: ")
price = float(input("Unit price: "))
quantity = int(input("Quantity: "))
subtotal = price * quantity
member = input("Are you a member? (yes/no):")
if member == "yes":
    discount_rate = 0.1
else:
    discount_rate = 0
discount = subtotal * discount_rate
after_discount = subtotal - discount
gst_rate = 0.15
gst = gst_rate * after_discount
total = after_discount + gst

