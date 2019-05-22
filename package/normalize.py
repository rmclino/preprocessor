from .preprocessor import Preprocessor

class Normalize(Preprocessor):
   
    """ Normiliza class for receive data and return normalized data
    
            No Attributes   
    """

    def normalize(self, tipo = 'sample'):
        if len(self.data) > 1:
            self.get_mean()
            self.get_stdev(tipo)
            self.data = [ (x - self.mean) / self.stdev for x in self.data]
            return self.data
        else:
            print("Fill data points to Rescale")
    