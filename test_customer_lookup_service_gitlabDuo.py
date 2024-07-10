import unittest
from unittest.mock import patch
from customer_lookup_service import Customer, CustomerService

class TestCustomer(unittest.TestCase):
    """
    Test cases for the Customer class.
    """

    @patch('random.randint', return_value=1234)
    def test_customer_init(self, mock_random):
        """
        Test the initialization of the Customer class.
        Mocks the random.randint function to ensure a consistent customer_id.
        """
        customer = Customer("John Doe", "12345678", "12-34-56", "personal")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.account_number, "12345678")
        self.assertEqual(customer.sort_code, "12-34-56")
        self.assertEqual(customer.customer_id, 1234)
        self.assertEqual(customer.customer_type, "personal")

class TestCustomerService(unittest.TestCase):
    """
    Test cases for the CustomerService class.
    """

    def setUp(self):
        """
        Set up the initial state for the customer service tests.
        """
        self.service = CustomerService()
        self.customer1 = Customer("John Doe", "12345678", "12-34-56", "personal")
        self.customer2 = Customer("Jane Smith", "87654321", "65-43-21", "business")
        self.service.add_customer(self.customer1)
        self.service.add_customer(self.customer2)

    def test_add_customer(self):
        """
        Test adding a new customer to the service.
        """
        customer = Customer("Alice Johnson", "11223344", "11-22-33", "personal")
        self.service.add_customer(customer)
        self.assertEqual(len(self.service.customers), 3)
        self.assertIn(customer, self.service.customers)

    def test_find_customer_by_account_number(self):
        """
        Test finding a customer by account number.
        """
        results = self.service.find_customer(account_number="12345678")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], self.customer1)

    def test_find_customer_by_sort_code(self):
        """
        Test finding a customer by sort code.
        """
        results = self.service.find_customer(sort_code="65-43-21")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], self.customer2)

    def test_find_customer_by_customer_type(self):
        """
        Test finding customers by customer type.
        """
        results = self.service.find_customer(customer_type="business")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], self.customer2)

    def test_find_customer_by_multiple_criteria(self):
        """
        Test finding customers by multiple criteria (account number, sort code, and customer type).
        """
        results = self.service.find_customer(account_number="12345678", sort_code="12-34-56", customer_type="personal")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], self.customer1)

    def test_find_customer_with_no_match(self):
        """
        Test finding customers with criteria that do not match any customer.
        """
        results = self.service.find_customer(account_number="99999999")
        self.assertEqual(len(results), 0)

    def test_find_customer_with_no_criteria(self):
        """
        Test finding all customers when no criteria are given.
        """
        results = self.service.find_customer()
        self.assertEqual(len(results), 2)
        self.assertIn(self.customer1, results)
        self.assertIn(self.customer2, results)

if __name__ == '__main__':
    unittest.main()