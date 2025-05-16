import pytest
from customer import Customer

class TestCustomer:
    """Test cases for the Customer class"""
    
    def test_customer_initialization_with_valid_name(self):
        """Test that a customer can be initialized with a valid name"""
        customer = Customer("John Doe")
        assert customer.name == "John Doe"
    
    def test_name_property_getter(self):
        """Test that the name getter returns the correct value"""
        customer = Customer("Jane Smith")
        assert customer.name == "Jane Smith"
    
    def test_name_property_setter_valid(self):
        """Test that the name setter works with valid names"""
        customer = Customer("Original Name")
        customer.name = "New Valid Name"
        assert customer.name == "New Valid Name"
    
    def test_name_must_be_string(self):
        """Test that non-string names raise TypeError"""
        with pytest.raises(TypeError, match="Name must be a string"):
            Customer(123)
        
        customer = Customer("Valid")
        with pytest.raises(TypeError, match="Name must be a string"):
            customer.name = 456
    
    def test_name_length_validation(self):
        """Test that names must be between 1-15 characters"""
        # Test minimum length (1 character)
        customer = Customer("A")
        assert customer.name == "A"
        
        # Test maximum length (15 characters)
        max_length_name = "a" * 15
        customer = Customer(max_length_name)
        assert customer.name == max_length_name
        
        # Test too short (0 characters)
        with pytest.raises(ValueError, match="Name must be between 1 and 15 characters"):
            Customer("")
        
        # Test too long (16 characters)
        too_long_name = "a" * 16
        with pytest.raises(ValueError, match="Name must be between 1 and 15 characters"):
            Customer(too_long_name)
        
        # Test changing to invalid length
        customer = Customer("Valid Name")
        with pytest.raises(ValueError, match="Name must be between 1 and 15 characters"):
            customer.name = too_long_name
        assert customer.name == "Valid Name"  # Original name unchanged
    
    def test_name_storage_uses_underscore_prefix(self):
        """Test that the name is stored in _name attribute"""
        customer = Customer("Test Name")
        assert hasattr(customer, "_name")
        assert customer._name == "Test Name"