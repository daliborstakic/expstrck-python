import unittest
from expense import Expense

class ExpenseTest(unittest.TestCase):
    def setUp(self):
        """ Test setUp method """
        self.exp1 = Expense("Eggs", 2.5)
        self.exp2 = Expense("Milk", 3.5)

    def test_name(self):
        """ Testing name attribute functionality """

        # If no parameters are provided
        with self.assertRaises(TypeError): 
            exp3 = Expense()

        # Testing getter and setter
        self.assertEqual(self.exp1.name, "Eggs")
        self.assertEqual(self.exp2.name, "Milk")

        self.exp1.name = "Chocolate"
        self.exp2.name = 'Carrot'

        self.assertEqual(self.exp1.name, "Chocolate")
        self.assertEqual(self.exp2.name, "Carrot")

    def test_cost(self):
        """ Testing cost attribute functionality """

        # If the cost is negative
        with self.assertRaises(ValueError):
            exp3 = Expense("Bag", -2)

        # Testing getter and setter
        with self.assertRaises(ValueError):
            self.exp1.cost = -2 # Cost cannot be negative

        self.assertEqual(self.exp1.cost, 2.5)
        self.assertEqual(self.exp2.cost, 3.5)

        self.exp1.cost = 10
        self.exp2.cost = 5

        self.assertEqual(self.exp1.cost, 10)
        self.assertEqual(self.exp2.cost, 5)


if __name__ == '__main__':
    """ Just so I can run it without python in the console """
    unittest.main()
