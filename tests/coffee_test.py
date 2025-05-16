
import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def test_average_price():
    
    espresso = Coffee("Espresso")
    lynn = Customer("Lynn")
    
    
    order1 = lynn.create_order(espresso, 4.5)
    order2 = lynn.create_order(espresso, 5.0)
    

    assert len(espresso.orders()) == 2

    assert espresso.average_price() == 4.75
    
    assert order1 in espresso.orders()
    assert order2 in espresso.orders()
    assert lynn in espresso.customers()
    assert lynn in espresso.customers()