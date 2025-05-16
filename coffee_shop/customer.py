

class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = [] 

    def create_order(self, coffee, price):

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
        from coffee_shop.order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        customers = {}
        for order in coffee.orders():
            customers[order.customer] = customers.get(order.customer, 0) + order.price
        return max(customers, key=customers.get) if customers else None

