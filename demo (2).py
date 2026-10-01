from food_delivery import Customer, DeliveryPartner, Restaurant, MenuItem


# 1. Register customer Priya with phone 9876543210 and address Bangalore.
priya = Customer("Priya", "9876543210", "Bangalore")

# 2. Register delivery partner Rajesh with vehicle Bike.
rajesh = DeliveryPartner("Rajesh", "9999999999", "Bike")

# 3. Create Bawarchi at MG Road and add Biryani and Kebab.
bawarchi = Restaurant("Bawarchi", "MG Road")

biryani = MenuItem("Biryani", 250, False)
kebab = MenuItem("Kebab", 200, False)

bawarchi.add_item(biryani)
bawarchi.add_item(kebab)


# 4. Top up Priya's wallet by 500, then attempt a top-up of -100.
print("=== WALLET ===")
priya.add_to_wallet(500)
print("After adding 500:", priya._wallet_balance)

priya.add_to_wallet(-100)
print("After attempting to add -100:", priya._wallet_balance)


# 5. Priya places an order for Biryani and Kebab.
print("\n=== ORDER ===")
order = priya.place_order(bawarchi, [biryani, kebab])

# For this demo, use the requested OTP 1234.
# The Order class normally generates a random OTP.
order._otp = 1234


# 6. Print subtotal, GST, packaging fee, total, and estimated delivery time.
print("Order ID:", order._order_id)

subtotal = sum(item.price for item in order._items)
gst = subtotal * 0.05
packaging_fee = 20
total = order.calculate_bill()

print("Subtotal:", subtotal)
print("GST:", gst)
print("Packaging fee:", packaging_fee)
print("Total:", total)
print("Estimated delivery time:", order.estimated_time(), "minutes")


# 7. Rajesh accepts the order. Try a wrong OTP, then deliver using 1234.
print("\n=== DELIVERY ===")

rajesh.accept_order(order)
print("Order status after acceptance:", order._status)

print("Trying wrong OTP: 9999")
rajesh.deliver(order, 9999)
print("Order status after wrong OTP:", order._status)

print("Delivering with OTP: 1234")
rajesh.deliver(order, 1234)
print("Order status after correct OTP:", order._status)


# 8. Notify Priya and Rajesh using notify("Order delivered").
print("\n=== NOTIFICATIONS ===")
priya.notify("Order delivered")
rajesh.notify("Order delivered")
