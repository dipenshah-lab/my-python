import unittest
from customer_lookup_service import CustomerService, Customer


class TestCustomerService(unittest.TestCase):

    def setUp(self):
        self.service = CustomerService()

    def test_init(self):
        # Test that the customers list is initialized empty
        self.assertEqual(len(self.service.customers), 0)

    def test_add_customer(self):
        # Test adding a customer
        customer = Customer("John Doe", "12345678", "12-34-56", "personal")
        self.service.add_customer(customer)
        self.assertEqual(len(self.service.customers), 1)
        self.assertEqual(self.service.customers[0].name, "John Doe")

    def test_find_customer_no_filters(self):
        # Test finding customers with no filters
        customer1 = Customer("John Doe", "12345678", "12-34-56", "personal")
        customer2 = Customer("Jane Doe", "87654321", "65-43-21", "business")
        self.service.add_customer(customer1)
        self.service.add_customer(customer2)

        results = self.service.find_customer()
        self.assertEqual(len(results), 2)
        self.assertIn(customer1, results)
        self.assertIn(customer2, results)

    def test_find_customer_by_account_number(self):
        # Test finding customer by account number
        customer1 = Customer("John Doe", "12345678", "12-34-56", "personal")
        customer2 = Customer("Jane Doe", "87654321", "65-43-21", "business")
        self.service.add_customer(customer1)
        self.service.add_customer(customer2)

        results = self.service.find_customer(account_number="12345678")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], customer1)

    def test_find_customer_by_sort_code(self):
        # Test finding customer by sort code
        customer1 = Customer("John Doe", "12345678", "12-34-56", "personal")
        customer2 = Customer("Jane Doe", "87654321", "65-43-21", "business")
        self.service.add_customer(customer1)
        self.service.add_customer(customer2)

        results = self.service.find_customer(sort_code="65-43-21")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], customer2)

    def test_find_customer_by_customer_type(self):
        # Test finding customer by customer type
        customer1 = Customer("John Doe", "12345678", "12-34-56", "personal")
        customer2 = Customer("Jane Doe", "87654321", "65-43-21", "business")
        self.service.add_customer(customer1)
        self.service.add_customer(customer2)

        results = self.service.find_customer(customer_type="business")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], customer2)


if __name__ == '__main__':
    unittest.main()