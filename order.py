class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = None  # Initialize private attribute
        self.price = price  # Use property setter for validation
        
    @property
    def price(self):
        """Getter returns the order price"""
        return self._price
    
    @price.setter
    def price(self, value):
        """Setter enforces price validation rules"""
        if self._price is not None:
            raise AttributeError("Order price cannot be changed after initialization")
        
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        
        self._price = value