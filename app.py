import streamlit as st
from food_delivery import Customer, DeliveryPartner, MenuItem, Restaurant

st.set_page_config(
    page_title="OOP Food Delivery",
    page_icon="🍔",
    layout="wide",
)

st.title("🍔 OOP Food Delivery System")
st.caption("Simple Streamlit interface for the food-delivery OOP project")

# -----------------------------
# Demo restaurant / menu
# -----------------------------
if "restaurant" not in st.session_state:
    restaurant = Restaurant("Food Corner", "Aurangabad")
    restaurant.add_item(MenuItem("Veg Burger", 120, True))
    restaurant.add_item(MenuItem("Paneer Pizza", 250, True))
    restaurant.add_item(MenuItem("Chicken Biryani", 220, False))
    restaurant.add_item(MenuItem("French Fries", 90, True))
    restaurant.add_item(MenuItem("Cold Drink", 50, True))
    st.session_state.restaurant = restaurant

if "customer" not in st.session_state:
    st.session_state.customer = None

if "partner" not in st.session_state:
    st.session_state.partner = None

if "order" not in st.session_state:
    st.session_state.order = None

restaurant = st.session_state.restaurant

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("Navigation")
    section = st.radio(
        "Choose a section",
        [
            "1. Create Customer",
            "2. Add Wallet Balance",
            "3. Restaurant Menu",
            "4. Place Order",
            "5. Create Delivery Partner",
            "6. Accept Order",
            "7. Complete Delivery",
        ],
    )

# -----------------------------
# 1. Create customer
# -----------------------------
if section == "1. Create Customer":
    st.header("👤 Create Customer")

    with st.form("customer_form"):
        name = st.text_input("Customer Name")
        phone = st.text_input("Phone Number")
        address = st.text_area("Delivery Address")
        submitted = st.form_submit_button("Create Customer")

    if submitted:
        if not name or not phone or not address:
            st.error("Please fill in all fields.")
        else:
            st.session_state.customer = Customer(name, phone, address)
            st.session_state.order = None
            st.success(f"Customer '{name}' created successfully.")

    if st.session_state.customer:
        customer = st.session_state.customer
        st.subheader("Customer Profile")
        st.write(f"**Name:** {customer._name}")
        st.write(f"**Phone:** {customer._phone}")
        st.write(f"**Address:** {customer.address}")
        st.write(f"**Wallet Balance:** ₹{customer._wallet_balance:.2f}")

# -----------------------------
# 2. Wallet
# -----------------------------
elif section == "2. Add Wallet Balance":
    st.header("💰 Add Wallet Balance")

    customer = st.session_state.customer
    if not customer:
        st.warning("Create a customer first.")
    else:
        st.write(f"Current balance: **₹{customer._wallet_balance:.2f}**")

        with st.form("wallet_form"):
            amount = st.number_input(
                "Amount to add",
                min_value=0.0,
                step=50.0,
                value=100.0,
            )
            submitted = st.form_submit_button("Add Money")

        if submitted:
            customer.add_to_wallet(amount)
            st.success(f"₹{amount:.2f} added to wallet.")
            st.metric("Wallet Balance", f"₹{customer._wallet_balance:.2f}")

# -----------------------------
# 3. Restaurant menu
# -----------------------------
elif section == "3. Restaurant Menu":
    st.header("🍽️ Restaurant Menu")
    st.write(f"**{restaurant.name}** — {restaurant.location}")

    menu = restaurant.get_menu()

    for i, item in enumerate(menu):
        veg = "🟢 Veg" if item.is_veg else "🔴 Non-Veg"
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            st.write(f"**{item.name}**")
        with col2:
            st.write(veg)
        with col3:
            st.write(f"₹{item.price:.2f}")

# -----------------------------
# 4. Place order
# -----------------------------
elif section == "4. Place Order":
    st.header("🛒 Place an Order")

    customer = st.session_state.customer
    if not customer:
        st.warning("Create a customer first.")
    else:
        menu = restaurant.get_menu()

        selected_names = st.multiselect(
            "Select food items",
            [item.name for item in menu],
        )

        selected_items = [
            item for item in menu if item.name in selected_names
        ]

        if selected_items:
            st.subheader("Order Summary")
            subtotal = sum(item.price for item in selected_items)
            gst = subtotal * 0.05
            packaging = 20
            total = subtotal + gst + packaging

            for item in selected_items:
                st.write(f"- {item.name}: ₹{item.price:.2f}")

            st.write(f"**Subtotal:** ₹{subtotal:.2f}")
            st.write(f"**GST (5%):** ₹{gst:.2f}")
            st.write(f"**Packaging:** ₹{packaging:.2f}")
            st.write(f"### Total: ₹{total:.2f}")

            if st.button("Place Order", type="primary"):
                if customer._wallet_balance < total:
                    st.error(
                        f"Insufficient wallet balance. "
                        f"Required ₹{total:.2f}, available ₹{customer._wallet_balance:.2f}."
                    )
                else:
                    order = customer.place_order(restaurant, selected_items)
                    customer._wallet_balance -= total
                    st.session_state.order = order
                    st.success(f"Order #{order._order_id} placed successfully.")
                    st.info(
                        f"Delivery OTP: **{order._otp}** "
                        "(shown here for demo/testing)"
                    )
        else:
            st.info("Select at least one menu item.")

# -----------------------------
# 5. Create delivery partner
# -----------------------------
elif section == "5. Create Delivery Partner":
    st.header("🛵 Create Delivery Partner")

    with st.form("partner_form"):
        name = st.text_input("Partner Name")
        phone = st.text_input("Partner Phone")
        vehicle = st.selectbox("Vehicle", ["Bike", "Scooter", "Car"])
        submitted = st.form_submit_button("Create Delivery Partner")

    if submitted:
        if not name or not phone:
            st.error("Please fill in name and phone.")
        else:
            st.session_state.partner = DeliveryPartner(name, phone, vehicle)
            st.success(f"Delivery partner '{name}' created successfully.")

    if st.session_state.partner:
        partner = st.session_state.partner
        st.subheader("Partner Profile")
        st.write(f"**Name:** {partner._name}")
        st.write(f"**Phone:** {partner._phone}")
        st.write(f"**Vehicle:** {partner.vehicle}")
        st.write(f"**Available:** {'Yes' if partner.is_available else 'No'}")

# -----------------------------
# 6. Accept order
# -----------------------------
elif section == "6. Accept Order":
    st.header("📦 Accept Order")

    order = st.session_state.order
    partner = st.session_state.partner

    if not order:
        st.warning("Place an order first.")
    elif not partner:
        st.warning("Create a delivery partner first.")
    else:
        st.write(f"**Order ID:** #{order._order_id}")
        st.write(f"**Current Status:** {order._status}")
        st.write(f"**Bill:** ₹{order.calculate_bill():.2f}")
        st.write(f"**Estimated Time:** {order.estimated_time()} minutes")

        if not partner.is_available:
            st.warning("Delivery partner is currently unavailable.")
        elif order._status == "Delivered":
            st.success("This order has already been delivered.")
        else:
            if st.button("Accept Order", type="primary"):
                partner.accept_order(order)
                st.success(f"Order #{order._order_id} accepted.")
                st.write(f"**New Status:** {order._status}")

# -----------------------------
# 7. Complete delivery
# -----------------------------
elif section == "7. Complete Delivery":
    st.header("🔐 Complete Delivery")

    order = st.session_state.order
    partner = st.session_state.partner

    if not order:
        st.warning("Place an order first.")
    elif not partner:
        st.warning("Create a delivery partner first.")
    else:
        st.write(f"**Order ID:** #{order._order_id}")
        st.write(f"**Order Status:** {order._status}")

        if order._status not in ["Accepted", "Order Accepted"]:
            st.info("The order must be accepted before delivery can be completed.")
        else:
            otp = st.text_input("Enter 4-digit OTP", max_chars=4)

            if st.button("Complete Delivery", type="primary"):
                if not otp.isdigit() or len(otp) != 4:
                    st.error("Enter a valid 4-digit OTP.")
                elif partner.deliver(order, int(otp)):
                    st.success("🎉 Delivery completed successfully!")
                    st.write(f"**Order Status:** {order._status}")
                    st.write(
                        f"**Partner Available:** "
                        f"{'Yes' if partner.is_available else 'No'}"
                    )
                else:
                    st.error("Invalid OTP. Delivery was not completed.")

# -----------------------------
# Current workflow status
# -----------------------------
st.divider()
st.subheader("📊 Current Workflow Status")

cols = st.columns(4)

with cols[0]:
    st.metric(
        "Customer",
        "Created" if st.session_state.customer else "Not created",
    )

with cols[1]:
    st.metric(
        "Order",
        (
            f"#{st.session_state.order._order_id}"
            if st.session_state.order
            else "Not placed"
        ),
    )

with cols[2]:
    st.metric(
        "Delivery Partner",
        "Created" if st.session_state.partner else "Not created",
    )

with cols[3]:
    st.metric(
        "Order Status",
        st.session_state.order._status
        if st.session_state.order
        else "—",
    )
