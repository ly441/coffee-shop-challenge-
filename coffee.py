


class Coffee:
    def __init__(self, name):
        self._name = None  # Initialize private attribute
        self.name = name
        self._orders = []
        
           # Use property setter for validation
        
    @property
    def name(self):
       
       
        return self._name
    
    @name.setter
    def name(self, value):
       
       
        if self._name is not None:
            raise AttributeError("Coffee name cannot be changed after initialization")
        
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        
        self._name = value
    def orders(self):
        return self._orders
    def customers(self):
        return list({order.customer for order in self._orders})   
    def customers(self):
        return list({order.customer for order in self._orders})
    def num_orders(self):
        return len(self._orders)
    def avaerage_price(self):
        if not self._orders:
            return 0.0
        return sum(order.price for order in self._orders) / len(self._orders)
        
