class Sort_Algorithm():

    def __init__(self, item_list) -> None:
        self.item_list = item_list

        pass

    def Bubble_sort(self):
        swap_again = True 
        n = len(self.item_list)
        while n > 0 and swap_again == True:
            n = n-1
            swap_again == False

            for i in range(n):
                if self.item_list[i] > self.item_list[i+1]:
                    self.item_list[i], self.item_list[i+1] = self.item_list[i+1], self.item_list[i]
                    swap_again = True

        return self.item_list

        

    def Insertion_sort(self):
        n=len(self.item_list)

        for i in range(1,n):
            value  = self.item_list[i]
            j = i
            while j > 0 and self.item_list[j-1] > value:
                self.item_list[j] = self.item_list[j-1]
                j = j - 1
            self.item_list[j] = value
        
        return self.item_list


  