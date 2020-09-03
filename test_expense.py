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

if __name__ == '__main__':
    """ Just so I can run it without python in the console """
    unittest.main()
