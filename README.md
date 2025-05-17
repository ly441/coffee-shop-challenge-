# Coffee Shop Challenge

A Python OOP project that models a simple coffee shop system, allowing you to manage customers, coffees, and orders. This project demonstrates class relationships, data validation, and basic business logic.

## Features

- **Customer Management:** Create customers with validated names.
- **Coffee Management:** Define coffee types with strict name validation.
- **Order Processing:** Place orders linking customers and coffees, with price validation.
- **Relationship Tracking:** Easily retrieve which customers ordered which coffees, and vice versa.

## Project Structure

```
coffee-shop-challenge-/
├── coffee_shop/
│   ├── coffee.py      # Coffee class
│   ├── customer.py    # Customer class
│   └── order.py       # Order class
├── README.md
```

## Usage Example

```python
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

# Creating an order
customer1 = Customer("lynn")
coffee1 = Coffee("Espresso")

# Placing an order
order1 = Order(customer1, coffee1, 5.00)

# Access data
print(customer1.coffees())  
print(coffee1.customers())  
print(coffee1.num_orders()) 
```

## Running the Project

1. Clone this repository.
2. Ensure all `.py` files are in the `coffee_shop` directory.
3. Run any of the Python files to test functionality, for example:
   ```bash
   python3 coffee_shop/coffee.py
   ```