# In order.py
from customer import Customer
from coffee import Coffee
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        # Add this order to customer and coffee
        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Must be Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Must be Coffee instance")
        self._coffee = value

    @property
    def price(self):
        return self._price
    
    
    