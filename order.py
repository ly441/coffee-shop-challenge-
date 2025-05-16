
from customer import Customer  # Make sure to import Customer
from coffee import Coffee      # Make sure to import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        # Use property setters for validation
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        # Add to customer's and coffee's order lists
        customer.orders().append(self)
        coffee.orders().append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):  # Fixed syntax
            raise TypeError("Must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):  # Fixed syntax
            raise TypeError("Must be a Coffee instance")
        self._coffee = value

order1 = Order(customer1, coffee1, 5.00)