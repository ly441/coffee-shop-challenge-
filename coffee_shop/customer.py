

class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = [] 
         # Stores Order instances for this customer
    def create_order(self, coffee, price):
        # Move the import HERE instead of at the top
        from coffee_shop.order import Order
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        """Return list of all orders for this customer"""
        return self._orders

    def coffees(self):
        """Return unique list of coffees ordered"""
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        """Create and return a new Order linked to this customer"""
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        """Return customer who spent most on given coffee"""
        if not coffee.orders():
            return None
            
        customers_spending = {}
        for order in coffee.orders():
            if order.customer not in customers_spending:
                customers_spending[order.customer] = 0
            customers_spending[order.customer] += order.price
            
        return max(customers_spending, key=lambda k: customers_spending[k])


