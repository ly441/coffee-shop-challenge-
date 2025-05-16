
import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def test_num_orders_and_average_price():
    
    espresso = Coffee("Espresso")
    lynn = Customer("Lynn")
    
    
    order1 = lynn.create_order(espresso, 4.5)
    order2 = lynn.create_order(espresso, 5.0)
    

    assert espresso.num_orders() == 2
    assert espresso.average_price() == pytest.approx(4.75)  # Handle floating point precision
    

    assert order1 in espresso.orders()
    assert order2 in espresso.orders()
    assert lynn in espresso.customers()
    assert lynn in espresso.customers()