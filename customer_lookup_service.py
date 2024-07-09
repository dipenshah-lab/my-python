import random

# This script defines a simple customer lookup service.
# The CustomerService class allows adding and searching for customers by account number, sort code, and customer type.

class Customer:
    def __init__(self, name, account_number, sort_code, customer_type):
        # Initialize the customer with name, account number, sort code, and customer type
        self.name = name
        self.account_number = account_number
        self.sort_code = sort_code
        self.customer_id = random.randint(1000, 9999)  # unique customer ID
        self.customer_type = customer_type

class CustomerService:
    def __init__(self):
        # Initialize an empty list to hold the customers
        self.customers = []

    def add_customer(self, customer):
        # Add a new customer to the list
        self.customers.append(customer)

    def find_customer(self, account_number=None, sort_code=None, customer_type=None):
        # Search for customers based on account number, sort code, and customer type
        results = []
        for customer in self.customers:
            if (account_number is None or customer.account_number == account_number) and \
               (sort_code is None or customer.sort_code == sort_code) and \
               (customer_type is None or customer.customer_type == customer_type):
                results.append(customer)
        return results

# Example usage
service = CustomerService()
service.add_customer(Customer("John Doe", "12345678", "12-34-56", "personal"))
service.add_customer(Customer("Jane Smith", "87654321", "65-43-21", "business"))

# Search by account number
results = service.find_customer(account_number="12345678")
for customer in results:
    print(f"Found customer: {customer.name}, Account: {customer.account_number}, Sort Code: {customer.sort_code}, Type: {customer.customer_type}")

# Search by sort code
results = service.find_customer(sort_code="65-43-21")
for customer in results:
    print(f"Found customer: {customer.name}, Account: {customer.account_number}, Sort Code: {customer.sort_code}, Type: {customer.customer_type}")

# Search by customer type
results = service.find_customer(customer_type="business")
for customer in results:
    print(f"Found customer: {customer.name}, Account: {customer.account_number}, Sort Code: {customer.sort_code}, Type: {customer.customer_type}")
