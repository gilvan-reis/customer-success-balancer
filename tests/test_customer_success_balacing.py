import unittest
import time

from src.customer_success_balancing import balance_customers


class TestCustomerSuccessBalancing(unittest.TestCase):

    def create_dict(self, values):
        return [{'id': key, 'value': value} for key, value in enumerate(values, 1)]

    def test_scenario_one(self):
        # GIVEN
        css = self.create_dict([60, 20, 95, 75])
        customers = self.create_dict([90, 20, 70, 40, 60, 10])
        absent_css = [2, 4]

        expected_result = 1

        # WHEN
        result = balance_customers(css, customers, absent_css)

        # THEN
        self.assertEqual(result, expected_result)

    def test_scenario_two(self):
        # GIVEN
        css = self.create_dict([11, 21, 31, 3, 4, 5])
        customers = self.create_dict([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
        absent_css = []

        expected_result = 0

        # WHEN
        result = balance_customers(css, customers, absent_css)

        # THEN
        self.assertEqual(result, expected_result)

    def test_scenario_three(self):
        # GIVEN
        css = self.create_dict([0] * 1000)
        css[998]['value'] = 100
        customers = self.create_dict([10]* 10000)
        absent_css = [1000]

        expected_result = 999

        # WHEN
        start = time.time()
        result = balance_customers(css, customers, absent_css)
        end = time.time()

        # THEN
        self.assertEqual(result, expected_result)
        self.assertLessEqual(end - start, 1, 'Execution time must be lesser than one second')

    def test_scenario_four(self):
        # GIVEN
        css = self.create_dict([1, 2, 3, 4, 5, 6])
        customers = self.create_dict([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
        absent_css = []

        expected_result = 0

        # WHEN
        result = balance_customers(css, customers, absent_css)

        # THEN
        self.assertEqual(result, expected_result)

    def test_scenario_five(self):
        # GIVEN
        css = self.create_dict([100, 2, 3, 3, 4, 5])
        customers = self.create_dict([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
        absent_css = []

        expected_result = 1

        # WHEN
        result = balance_customers(css, customers, absent_css)

        # THEN
        self.assertEqual(result, expected_result)

    def test_scenario_six(self):
        # GIVEN
        css = self.create_dict([100, 99, 88, 3, 4, 5])
        customers = self.create_dict([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
        absent_css = [1, 3, 2]

        expected_result = 0

        # WHEN
        result = balance_customers(css, customers, absent_css)

        # THEN
        self.assertEqual(result, expected_result)

    def test_scenario_seven(self):
        # GIVEN
        css = self.create_dict([100, 99, 88, 3, 4, 5])
        customers = self.create_dict([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
        absent_css = [4, 5, 6]

        expected_result = 3

        # WHEN
        result = balance_customers(css, customers, absent_css)

        # THEN
        self.assertEqual(result, expected_result)

    def test_with_invalid_css(self):
        # GIVEN
        css_without_id = [{'value': 10}]
        css_without_value = [{'id': 1}]
        customers = self.create_dict([10])
        absent_css = []

        # WHEN / THEN
        with self.assertRaises(KeyError):
            balance_customers(css_without_id, customers, absent_css)

        with self.assertRaises(KeyError):
            balance_customers(css_without_value, customers, absent_css)

    def test_with_invalid_customers(self):
        # GIVEN
        css = self.create_dict([10])
        customers_without_id = [{'value': 10}]
        customers_without_value = [{'id': 1}]
        absent_css = []

        # WHEN / THEN
        with self.assertRaises(KeyError):
            balance_customers(css, customers_without_id, absent_css)

        with self.assertRaises(KeyError):
            balance_customers(css, customers_without_value, absent_css)
