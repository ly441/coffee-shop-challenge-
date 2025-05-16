

from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def test_create_order():
    lynn = Customer("Lynn")
    espresso = Coffee("Espresso")
    
    
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
    

    top_customer = Customer.most_aficionado(espresso)
    assert top_customer == lynn




if __name__ == "__main__":
    lynn = Customer("Lynn")
    espresso = Coffee("Espresso")
    
    
    order = lynn.create_order(espresso, 4.5)
    print(f"Order price: {order.price}")    