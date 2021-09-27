from _typeshed import Self
import unittest
from Luhn import luhner

class luhn(unittest.TestCase):

    def setUp(self) -> None:
        self.test_1 =luhner('553343434343434')
        self.test_2 =luhner('898339892323222')
        return super().setUp()
    def tearDown(self) -> None:
        return super().tearDown()


    def test_luhn(self):
        self.assertEqual(self.test_1.luhn(), True)

