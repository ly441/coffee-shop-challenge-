
from coffee import Coffee
from order import Order


class Customer:
    def __init__(self, name):
        self.name = name 
        self._orders =[]
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        
        self._name = value
    def orders(self):
        return self._orders
    def coffees(self):
        return list({order.coffee for order in self._orders})   


if __name__ == "__main__":
    # Create instances
    customer1 = Customer("Lynn")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    
    # Create orders linked to the customer
    Order(customer1, coffee1, 4.5)
    Order(customer1, coffee2, 5.0)
    
    # Print formatted output
    print(f"Customer: {customer1.name}")
    print(f"Total Orders: {len(customer1.orders())}")
    print("Coffees Ordered:")
    for coffee in customer1.coffees():
        print(f"- {coffee.name}")