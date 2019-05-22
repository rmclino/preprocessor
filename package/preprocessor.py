class Preprocessor:
   
    def __init__(self):
        self.fileName = None

        """ Pre processing class for receive data and return normalized data
    
            Attributes: fileName
    
        """
    
    def __repr__(self):
        return "Nome do Arquivo em estudo: {}".format(self.fileName)

    def load_file(self,fileName, outPutFile="out_put",type='txt'):
        
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
        self.fileName = fileName
        with open(fileName) as file:
            data_list = []
            line = file.readline()
            while line:
                try:
                    data_list.append(float(line))
                except:
                    data_list.append(line)
                    print("MissingValue")
                line = file.readline()
        file.close()
    
        self.data = data_list
        self.len = len(data_list)
        return print("Arquivo com : {} dados".format(self.len))
    
    def get_mean(self, digits=6):
        self.mean = None
        if self.data != None:
            self.mean = round( sum(self.data)/len(self.data), digits)
            return self.mean
        else:
            raise "No Data"
    
    def get_stdev(self, digits=6, tipo='amostra'):
        if tipo =='amostra':
            d = 1
        else:
            d = 0
            if self.len < 2:
                raise ValueError('Necessita pelo menos 2 dados')
        self.get_mean()
        self.variance = sum( (x - self.mean)**2 for x in self.data) / (self.len -d)
        self.stdev = round( self.variance **0.5 , 6)
        return self.stdev
        



def main():
    print("ditest")
    p = Preprocessor()
    p.load_file('data.txt')
    p.mean

if __name__ == 'main':
    main()