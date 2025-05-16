
import pytest
from customer import Customer
from coffee import Coffee

def test_create_order():
    lynn = Customer("Lynn")
    espresso = Coffee("Espresso")
    
    # Test order creation
    order1 = lynn.create_order(espresso, 4.5)
    order2 = lynn.create_order(espresso, 5.0)
    
    assert len(lynn.orders()) == 2
    assert espresso in lynn.coffees()

def test_most_aficionado():
    # Setup
    lynn = Customer("Lynn")
    annah = Customer("Annah")
    espresso = Coffee("Espresso")
    
    # Lynn orders espresso twice
    lynn.create_order(espresso, 4.5)
    lynn.create_order(espresso, 5.0)
    
    # Annah orders once
    annah.create_order(espresso, 4.0)
    
    # Test
    top_customer = Customer.most_aficionado(espresso)
    assert top_customer == lynn