# Food Delivery System

A modern Python-based food delivery simulation built with Object-Oriented Programming (OOP) principles. This project demonstrates how a food ordering platform can be modeled using classes, inheritance, encapsulation, and polymorphism in a clean and understandable way.

The repository includes:
- a core business logic layer for customers, restaurants, orders, and delivery partners
- a Streamlit-based interactive interface for end-to-end demo usage
- a sample script showing the order and delivery flow
- a Jupyter Notebook version for experimentation and presentation

## Project Overview

This system models a simplified food delivery workflow where a customer can:
- create an account
- add money to a wallet
- browse a restaurant menu
- place an order
- receive an OTP for delivery verification

A delivery partner can:
- register as available for delivery
- accept assigned orders
- deliver the order after OTP verification

## Features

- Customer wallet management
- Restaurant menu with veg/non-veg item classification
- Order creation with automatic order ID generation
- GST and packaging fee calculation
- Estimated delivery time
- OTP-based delivery validation
- Order status tracking: Placed → Accepted → Delivered
- Interactive UI built with Streamlit

## Tech Stack

- Python 3
- Streamlit
- Object-Oriented Programming (OOP)
- Jupyter Notebook

## Repository Structure

```text
Food-Delivery-System/
├── app.py                     # Streamlit UI for the food delivery app
├── food_delivery.py           # Core OOP logic and class definitions
├── demo (2).py                # Demo script showcasing the workflow
├── Food_Delivery_System.ipynb # Jupyter notebook version of the project
├── Requirements.txt           # Python dependencies
├── README.md                 # Project documentation
└── .gitignore                # Git ignore file (if present in repo)
```

## Core Classes

The system is structured around the following classes:

- `User` - Abstract base class with shared user properties like name, phone, and wallet balance
- `Customer` - Represents the end user who places orders and manages wallet funds
- `DeliveryPartner` - Represents a courier/delivery agent who accepts and validates deliveries
- `Restaurant` - Holds restaurant details and a menu list
- `MenuItem` - Represents a food item with name, price, and vegetarian status
- `Order` - Handles order ID, bill calculation, status tracking, and OTP verification

## OOP Concepts Demonstrated

- Abstraction: `User` is defined as an abstract class
- Inheritance: `Customer` and `DeliveryPartner` inherit from `User`
- Encapsulation: private/protected attributes are managed through methods
- Polymorphism: `notify()` and `display_profile()` behave differently for different user types

## How to Run

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

## Example Workflow

1. Create a customer and assign a delivery address
2. Add wallet balance
3. Browse the restaurant menu
4. Place an order for selected items
5. Generate the order bill with GST and packaging fee
6. Delivery partner accepts the order
7. OTP is verified to complete the delivery

## Sample Order Calculation

The project calculates total cost as:

```text
Subtotal + GST (5%) + Packaging Fee (₹20)
```

Example:

```text
Subtotal: ₹500
GST: ₹25
Packaging: ₹20
Total: ₹545
```

## Benefits of the Project

- Clear understanding of real-world object modeling in Python
- Good beginner-friendly example of OOP concepts
- Easy to extend for features like inventory management, order history, and admin controls
- Suitable for academic projects, demos, and interviews

## Future Enhancements

- Randomized OTP generation per order
- Automatic partner assignment based on availability
- Order cancellation and additional order states
- Ratings and reviews
- Database storage for persistent records
- Unit tests with `pytest`
- Admin dashboard for restaurant management

## License

This project is currently distributed without a formal license declaration. If you want to publish it publicly, consider adding an appropriate open-source license such as MIT.

## Author

Ambika1794

## Contact

For questions or suggestions, feel free to reach out through the GitHub repository.
