class Search_Algorithm():

    def __init__(self, Items, Items_to_find ) -> None:
        self.Items = Items
        self.Items_to_find = Items_to_find
        found = ''
        

    def binary_search(self):
        counter = 0
        self.found = False

        while self.found == False and  counter < len(self.Items):

            if self.Items[counter] == self.Items_to_find:
                self.found =True

                return self.found
            else:
                counter = counter +1 

        return self.found

    
        

case_1 = Search_Algorithm([8,9,7],7)
case_1.binary_search
print(case_1.binary_search())