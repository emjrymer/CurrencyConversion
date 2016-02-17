import unittest
from conversion_functions import convert_usd_to_eur, convert_eur_to_usd, convert_multi_entries_eur_to_usd, convert_multi_entries_usd_to_eur, register_usd_to_eur, register_eur_to_usd, proper_input#, valid_input


# USD -----> EUR
class UsdToEurTestCase(unittest.TestCase):

    def test_convert_one_usd_to_eur(self):
        # assert convert_usd_to_eur(1) == 0.9
        self.assertEqual(convert_usd_to_eur(1), 0.9)

    def test_convert_three_usd_to_eur(self):
        # assert convert_usd_to_eur(3) == 2.7
        self.assertEqual(convert_usd_to_eur(3), 2.7)

    def test_convert_one_and_fifty_cents_to_eur(self):
        # assert convert_usd_to_eur(1.50) == 1.35
        self.assertEqual(convert_usd_to_eur(1.50), 1.35)

    def test_sum_values_usd_to_eur(self):
        self.assertEqual(convert_multi_entries_usd_to_eur([1.4, 3.6, 2.3]), 6.57)

    def test_register_usd_to_eur(self):
        self.assertEqual(register_usd_to_eur([1, 3, 1.50]), [0.9, 2.7, 1.35])

    # def test_register_ute_str(self):
        # self.assertEqual(register_usd_to_eur("1, 3, 1.5"), [0.9, 2.7, 1.35])

# EUR -----> USD
class EurToUsdTestCase(unittest.TestCase):

    def test_convert_one_eur_to_usd(self):
        self.assertEqual(convert_eur_to_usd(1), 1.11)

    def test_convert_three_eur_to_usd(self):
        self.assertEqual(convert_eur_to_usd(3), 3.33)

    def test_convert_one_and_fifty_eur_to_usd(self):
        self.assertEqual(convert_eur_to_usd(1.50), 1.67)

    def test_sum_values_eur_to_usd(self):
        self.assertEqual(convert_multi_entries_eur_to_usd([1.4, 3.6, 2.3]), 8.10)

    def test_register_eur_to_usd(self):
        self.assertEqual(register_eur_to_usd([1, 3, 1.50]), [1.11, 3.33, 1.67])

    def test_register_eur_to_usd_two(self):
        self.assertEqual(register_eur_to_usd([3, 1, 1.50]), [3.33, 1.11, 1.67])


'''class ValidInputTestCase(unittest.TestCase):

    def test_valid_input_proper_value(self):
        self.assertEqual(valid_input(7), 7)

    def test_valid_input_negative_value(self):
        self.assertEqual(valid_input(-2), "Not a proper value. ")

    def test_valid_input_alpha_value(self):
        self.assertEqual(valid_input("a"), "Not a proper value. ")'''

assert proper_input([1, 2]) == 1, 2
# assert proper_input([7, 3, 10, 'srrt']) == [7, 3, 10, 'not a proper input']
assert proper_input('a') == 'not a proper input'
