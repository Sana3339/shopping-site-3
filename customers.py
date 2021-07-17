"""Customers at Ubermelon."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return f'<Name = {self.first_name} {self.last_name}, email = {self.email}>'

def read_customer_types_from_file(filepath):
    """Read and format customer information from text file and populate dictionary of customers.

    Dictionary format will be: {email: Customer object}
    """

    customer_dictionary = {}

    with open(filepath) as file:
        for line in file:
            first_name, last_name, email, password = line.strip().split("|")
            customer_dictionary[email] = Customer(first_name, last_name, email, password)

    return customer_dictionary


def get_by_email(email):
    """Given an email, returns the customer object."""

    return customer_dictionary[email]



#Global variable that all functions have access to
customer_dictionary = read_customer_types_from_file("customers.txt")