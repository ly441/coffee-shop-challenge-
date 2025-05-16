
import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

@pytest.fixture
def sample_customer():
    return Customer("Test Customer")

@pytest.fixture
def sample_coffee():
    return Coffee("Test Coffee")

class TestOrder:
    def test_order_creation(self, sample_customer, sample_coffee):
        """Test valid order creation"""
        order = Order(sample_customer, sample_coffee, 5.0)
        assert order.price == 5.0
        assert order.customer == sample_customer
        assert order.coffee == sample_coffee

    def test_invalid_customer_type(self, sample_coffee):
        """Test non-Customer instance for customer"""
        with pytest.raises(TypeError):
            Order("not a customer", sample_coffee, 5.0)

    def test_invalid_coffee_type(self, sample_customer):
        """Test non-Coffee instance for coffee"""
        with pytest.raises(TypeError):
            Order(sample_customer, "not a coffee", 5.0)

    def test_price_validation(self, sample_customer, sample_coffee):
        """Test price type and range enforcement"""
        # Test string instead of float
        with pytest.raises(TypeError):
            Order(sample_customer, sample_coffee, "5")
            
        # Test too low
        with pytest.raises(ValueError):
            Order(sample_customer, sample_coffee, 0.99)
            
        # Test too high
        with pytest.raises(ValueError):
            Order(sample_customer, sample_coffee, 10.01)

    def test_price_immutability(self, sample_customer, sample_coffee):
        """Test price can't be changed after initialization"""
        order = Order(sample_customer, sample_coffee, 5.0)
        with pytest.raises(AttributeError):
            order.price = 6.0

    def test_relationship_management(self, sample_customer, sample_coffee):
        """Test order appears in customer's and coffee's order lists"""
        order = Order(sample_customer, sample_coffee, 5.0)
        
        # Check customer relationships
        assert order in sample_customer.orders()
        assert sample_coffee in sample_customer.coffees()
        
        # Check coffee relationships
        assert order in sample_coffee.orders()
        assert sample_customer in sample_coffee.customers()