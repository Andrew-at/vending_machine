import unittest

from source import MenuItem, SalesForDay, VendingMachine

class TestLemonadeStand(unittest.TestCase):

    def test_1(self):
        """Test get name method for MenuItem class"""
        menu_1 = MenuItem('Buzzy Lemonade', 3.00, 5.00)
        self.assertEqual(menu_1.get_name(), 'Buzzy Lemonade')

    def test_2(self):
        """Test get wholesale cost method for MenuItem class"""
        menu_1 = MenuItem('Buzzy Lemonade', 3.00, 5.00)
        self.assertEqual(menu_1.get_cost(), 3.00)

    def test_3(self):
        """Test get selling price for MenuItem class"""
        menu_1 = MenuItem('Buzzy Lemonade', 3.00, 5.00)
        self.assertEqual(menu_1.get_selling_price(), 5.00)

    def test_4(self):
        pass

    def test_5(self):
        pass

if __name__ == "__main__":
    unittest.main()
