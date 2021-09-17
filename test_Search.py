import unittest
from Search import Search_Algorithm

class Binary(unittest.TestCase):


    def setUp(self) -> None:
        self.search = Search_Algorithm([23,30,31,80],80)
        self.search_1 = Search_Algorithm(['a','b','c','d','e','f','h'], 'f')
        
    def tearDown(self) -> None:

        return super().tearDown()

    def test_linear(self):
        self.assertEqual(self.search.Linear_search(),True)
        self.assertEqual(self.search_1.Linear_search(), True)
        


    def test_binary(self):
        self.assertEqual(self.search_1.Binary_search(), True)
        self.assertEqual(self.search.Binary_search(), True)
         

    

if __name__ =='__main__':
    unittest.main()
