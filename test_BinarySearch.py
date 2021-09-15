import unittest
from Binary_Search import Search_Algorithm

class Binary(unittest.TestCase):

    def setUp(self) -> None:
        self.search = Search_Algorithm([8,2,31,8],8)
        self.search_1 = Search_Algorithm(['a','b','c','d','e','f','h'], 'f')
        
    def tearDown(self) -> None:
        return super().tearDown()

    def test_binary(self):
        self.assertEqual(self.search.binary_search(),True)
        self.assertEqual(self.search_1.binary_search(), True)

    def test_insertion(self):
        pass    

    

if __name__ =='__main__':
    unittest.main()
