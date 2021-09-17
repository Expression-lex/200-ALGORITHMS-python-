import unittest
from Sort import Sort_Algorithm

class Sort_Algo(unittest.TestCase):

    def setUp(self) -> None:
        self.list_1 = Sort_Algorithm([9,4,2])
        self.list_2 = Sort_Algorithm([8,5,9,1,3,7,3,0])

    def tearDown(self) -> None:
        return super().tearDown()

    def test_bubblesort(self):
        self.assertEqual = self.list_1.Bubble_sort(),[2,4,9]
        self.assertEqual = self.list_2.Bubble_sort(),[0,1,3,3,5,7,8,9]

    def test_insertionsort(self):
        self.assertEqual = self.list_2.Insertion_sort(),[2,4,9]
        self.assertEqual = self.list_1.Insertion_sort(),[0,1,3,3,5,7,8,9]