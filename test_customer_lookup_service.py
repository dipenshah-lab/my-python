import unittest
from unittest.mock import patch
from customer_lookup_service import Customer, CustomerService

# This set of unit tests aims to validate the functionality of the customer lookup service.
# The script includes several aspects that make writing unit tests challenging:
# 1. Random Customer ID: The Customer class generates a random customer ID, which is unpredictable and hard to assert in tests.
# 2. State Management: The CustomerService class's state changes dynamically, requiring careful setup and teardown for each test to ensure a clean state.

class TestCustomerService(unittest.TestCase):

    def setUp(self):
        # Set up the initial state for the customer service tests
        self.service = CustomerService()
        self.customer1 = Customer("John Doe", "12345678", "12-34-56", "personal")
        self.customer2 = Customer("Jane Smith", "87654321", "65-43-21", "business")
        self.service.add_customer(self.customer1)
        self.service.add_customer(self.customer2)

    def test_add_customer(self):
        # Test adding a new customer
        # Ensures a new customer can be added and subsequently found using their account number.
        customer = Customer("Alice Johnson", "11223344", "11-22-33", "personal")
        self.service.add_customer(customer)
        results = self.service.find_customer(account_number="11223344")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Alice Johnson")

    def test_find_customer_by_account_number(self):
        # Test finding a customer by account number
        # Verifies the ability to find a customer using their account number.
        results = self.service.find_customer(account_number="12345678")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "John Doe")

    def test_find_customer_by_sort_code(self):
        # Test finding a customer by sort code
        # Verifies the ability to find a customer using their sort code.
        results = self.service.find_customer(sort_code="65-43-21")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Jane Smith")

    def test_find_customer_by_customer_type(self):
        # Test finding customers by customer type
        # Verifies the ability to find customers by their customer type.
        results = self.service.find_customer(customer_type="business")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Jane Smith")

    def test_find_customer_by_multiple_criteria(self):
        # Test finding customers by multiple criteria
        # Tests finding a customer using multiple criteria (account number, sort code, and customer type).
        results = self.service.find_customer(account_number="12345678", sort_code="12-34-56", customer_type="personal")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "John Doe")

    def test_find_customer_with_no_match(self):
        # Test finding customers with criteria that do not match any customer
        # Ensures that searching with criteria that do not match any customer returns an empty list.
        results = self.service.find_customer(account_number="99999999")
        self.assertEqual(len(results), 0)

    def test_find_customer_with_no_criteria(self):
        # Test finding all customers when no criteria are given
        # Ensures that if no criteria are provided, all customers are returned.
        results = self.service.find_customer()
        self.assertEqual(len(results), 2)
        self.assertIn(self.customer1, results)
        self.assertIn(self.customer2, results)

    @patch('random.randint', return_value=1234)
    def test_customer_id(self, mock_random):
        # Test the customer ID generation based on a mocked random number
        # Uses mocking to test the random customer ID generation.
        customer = Customer("Mocked Customer", "00000000", "00-00-00", "mocked")
        self.assertEqual(customer.customer_id, 1234)

if __name__ == '__main__':
    unittest.main()

