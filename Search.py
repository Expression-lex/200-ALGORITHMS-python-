from Sort import Sort_Algorithm
class Search_Algorithm():

    def __init__(self, Items, Items_to_find ) -> None:
        self.Items = Items
        self.Items_to_find = Items_to_find
        found = ''
        

    def Linear_search(self):
        counter = 0
        found = False

        while found == False and  counter < len(self.Items):

            if self.Items[counter] == self.Items_to_find:
                found =True

                return found
            else:
                counter = counter + 1 

        return found

    def Binary_search(self):
        found = False
        first = 0
        last  = len(self.Items)-1
        
        self.Items = Sort_Algorithm(self.Items).Bubble_sort()


        while first <= last  and found == False:
            midpoint = (first + last)//2
            
            
            if self.Items[midpoint] == self.Items_to_find:
                found = True
            else:
                if self.Items[midpoint] < self.Items_to_find:
                    print(self.Items[midpoint])
                    first = midpoint + 1
                  
                else:
                    last = midpoint -1

            
        return found 

        # pass

case_1 = Search_Algorithm([2,3,5,19,45,98,900],900)
case_1
print(case_1.Binary_search())