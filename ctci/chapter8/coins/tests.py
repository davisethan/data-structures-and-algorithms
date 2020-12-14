import unittest
from CreateCentsStrategy import RecursiveCreateCentsStrategy
from Coin import Quarter, Dime, Nickel, Penny

class TestRecursiveCreateCentsStrategy(unittest.TestCase):
    def test_one_cents(self):
        cents = 1
        recursive_create_cents_strategy = RecursiveCreateCentsStrategy()

        cents_with_coins = recursive_create_cents_strategy.create_cents(cents)

        expected = {(Penny,)}
        self.assertEqual(expected, cents_with_coins)

    def test_five_cents(self):
        cents = 5
        recursive_create_cents_strategy = RecursiveCreateCentsStrategy()

        cents_with_coins = recursive_create_cents_strategy.create_cents(cents)

        expected = {(Penny, Penny, Penny, Penny, Penny,), (Nickel,)}
        self.assertEqual(expected, cents_with_coins)

    def test_six_cents(self):
        cents = 6
        recursive_create_cents_strategy = RecursiveCreateCentsStrategy()

        cents_with_coins = recursive_create_cents_strategy.create_cents(cents)

        expected = {(Nickel, Penny,), (Penny, Nickel,), (Penny, Penny, Penny, Penny, Penny, Penny,)}
        self.assertEqual(expected, cents_with_coins)

if __name__ == "__main__":
    unittest.main()
