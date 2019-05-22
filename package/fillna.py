from preprocessor import Preprocessor

class FillNa(Preprocessor):
    """
    FillNa class, to prepocess missing values

    """

    def fill_na(self,FillNaValue = 0):
        """ Function to fillNa with specific float value

        Args: FillNaValue a float number
        """
        if len(self.data) >0:
            list = []
            for value in self.data:
                try:
                    value = float(value)
                    list.append(value)
                except:
                    list.append(FillNaValue)
        self.data = list

        return self.data
    
    def fill_na_mean(self):
        """ Function to FillNa with the mean of valide Data 
            No Args
        """
        if len(self.data) >0:
            list = []
            for value in self.data:
                try:
                    value = float(value)
                    list.append(value)
                except:
                    print("missinge Value")
            FillNaValue = sum(list) / len(list)

            self.fill_na(FillNaValue)
        else:
            print("Revise o arquivo de dados")
    
