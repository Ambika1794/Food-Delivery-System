# 🍔 Food Delivery System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigm-OOP-6E9F18?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

</div>

A clean and beginner-friendly food delivery management project built in Python using Object-Oriented Programming (OOP). It simulates the core flow of a real food ordering system, including customer registration, wallet balance management, restaurant menu browsing, ordering, delivery partner assignment, and OTP-based delivery verification.

This project is designed for learning, demonstration, and academic use. It highlights important OOP principles such as abstraction, inheritance, encapsulation, and polymorphism in a practical business scenario.

## 🎯 Project Objectives

- To model a simplified real-world food delivery process in Python.
- To apply OOP concepts in a practical and understandable project.
- To build a customer-facing and partner-facing order workflow.
- To demonstrate order management, billing logic, and delivery verification.
- To provide a user-friendly UI using Streamlit for easy interaction.
- To support learning for students, beginners, and project showcases.

## 🌟 Key Features

- 👤 Customer profile creation with name, phone number, and delivery address
- 💰 Wallet-based payment simulation
- 🍽️ Restaurant menu with veg and non-veg item listing
- 🛒 Order placement with selected food items
- 📊 Automatic bill calculation including GST and packaging fee
- ⏱️ Estimated delivery time display
- 🔐 OTP-based order delivery verification
- 🚚 Delivery partner registration and order acceptance
- 📦 Order status tracking: Placed → Accepted → Delivered
- 🧠 Clean OOP class design for maintainability
- 🖥️ Interactive Streamlit dashboard for user experience

## 🏗️ System Overview

The project represents a simplified food delivery ecosystem with the following core components:

- Customer: places orders, adds money to wallet, and tracks order history
- Delivery Partner: accepts and delivers orders
- Restaurant: stores menu items and restaurant information
- MenuItem: defines each food item and its properties
- Order: stores items, status, amount, and OTP
- User: abstract base class shared by both customer and delivery partner

## 🧩 Core Classes and Responsibilities

| Class | Description |
| --- | --- |
| `User` | Abstract base class for shared user properties like name, phone, and wallet balance |
| `Customer` | Handles customer details, wallet top-up, order creation, and notifications |
| `DeliveryPartner` | Represents the delivery executive responsible for accepting and completing deliveries |
| `Restaurant` | Stores restaurant name, location, and menu items |
| `MenuItem` | Represents a food item with name, price, and vegetarian status |
| `Order` | Stores order details, calculates total amount, and verifies delivery OTP |

## 🔍 OOP Concepts Implemented

- Abstraction: `User` is an abstract class that defines common behavior.
- Inheritance: `Customer` and `DeliveryPartner` inherit from `User`.
- Encapsulation: attributes such as wallet balance, order status, and OTP are protected using method-based management.
- Polymorphism: `notify()` and `display_profile()` are implemented differently in subclass objects.

## 🧭 Project Workflow

1. Customer creates an account and provides delivery details.
2. Customer adds wallet balance.
3. User browses the restaurant menu.
4. Customer selects food items and places the order.
5. System calculates subtotal, GST, packaging fee, and final total.
6. Delivery partner accepts the order.
7. OTP is validated before the order is marked as delivered.
8. Final status is updated and order completion is confirmed.

## 📁 Repository Structure

```text
Food-Delivery-System/
├── app.py                     # Streamlit interface for running the app
├── food_delivery.py           # Core OOP logic and classes
├── demo (2).py                # Demo script for order flow simulation
├── Food_Delivery_System.ipynb # Notebook version of the project
├── Requirements.txt           # Python package requirements
├── README.md                 # Project documentation
└── .gitignore                # Git ignore settings
```

## 🛠️ Tech Stack

- Python 3
- Streamlit
- Jupyter Notebook
- Object-Oriented Programming (OOP)

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or above
- pip package manager
- Basic understanding of Python syntax

### 1. Clone the Repository

```bash
git clone https://github.com/Ambika1794/Food-Delivery-System.git
cd Food-Delivery-System
```

### 2. Install Dependencies

```bash
pip install -r Requirements.txt
```

### 3. Run the Streamlit Application

```bash
streamlit run app.py
```

### 4. Run the Demo Script

```bash
python "demo (2).py"
```

## 💡 Sample Usage Example

```python
restaurant = Restaurant("Spice Hub", "Aurangabad")
restaurant.add_item(MenuItem("Paneer Tikka", 180, True))
restaurant.add_item(MenuItem("Chicken Biryani", 250, False))

customer = Customer("Aman", "9876543210", "CIDCO, Aurangabad")
partner = DeliveryPartner("Rahul", "9123456780", "Bike")

customer.add_to_wallet(500)
order = customer.place_order(restaurant, restaurant.get_menu())

print("Total bill:", order.calculate_bill())
print("ETA:", order.estimated_time(), "minutes")

partner.accept_order(order)
partner.deliver(order, 1234)
customer.notify("Order delivered")
```

## 🧾 Billing Logic

The system calculates the order total using:

```text
Subtotal + 5% GST + ₹20 Packaging Fee
```

For example:

```text
Subtotal: ₹500
GST: ₹25
Packaging Fee: ₹20
Final Total: ₹545
```

## ✅ Benefits of This Project

- Easy to understand for beginners
- Strong demonstration of Python OOP concepts
- Realistic workflow for food-ordering business logic
- Can be expanded into a full-stack or database-backed version
- Suitable for academic projects, practical labs, and interviews

## 🚀 Future Enhancements

- Randomized OTP generation per order
- Real-time order tracking page
- Online payment simulation
- Restaurant admin panel
- Automatic delivery partner assignment
- Order cancellation and rescheduling
- Rating and review system
- Database integration using SQLite or MySQL
- Unit testing with `pytest`
- API-based backend support

## 📌 Project Highlights

- Beginner-friendly architecture
- Clean modular class design
- Visual demo through Streamlit
- Strong educational value
- Easy to extend with additional features

## 📝 License

This project is currently shared without a formal license declaration. If you plan to publish it publicly or share it commercially, adding an open-source license such as MIT is recommended.

## 👨‍💻 Author

Ambika1794

## 📬 Contact

Feel free to reach out through the GitHub repository for suggestions, improvements, or collaboration opportunities.
