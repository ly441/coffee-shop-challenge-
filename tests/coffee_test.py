

from customer import Customer
from coffee import Coffee

def test_num_orders_and_average_price():
    
    espresso = Coffee("Espresso")
    lynn = Customer("Lynn")
    
    # Create orders
    lynn.create_order(espresso, 4.5)
    lynn.create_order(espresso, 5.0)
    
    # Test
    assert espresso.num_orders() == 2
    assert espresso.average_price() == (4.5 + 5.0) / 2