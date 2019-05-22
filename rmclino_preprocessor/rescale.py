from .preprocessor import Preprocessor

class Rescale(Preprocessor):
   
    def rescale_MinMax(self):
        if len(self.data) > 1:
            self.max = max(self.data)
            self.min = min(self.data)
            factor = self.max - self.min
            self.data = [ x/factor for x in self.data]
            return self.data
        else:
            print("Fill data points to Rescale")
    
    def rescale_Factor(self, factor=1):

        if factor != 0:
            if len(self.data) > 1:
                self.max = max(self.data)
                self.min = min(self.data)
                factor = self.max - self.min
                self.data = [ x/factor for x in self.data]
                return self.data
            else:
                print("Fill data points to Rescale")
        else:
            print("Factor could note be 0")

