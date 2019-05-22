class Preprocessor:
   
    def __init__(self, fileName):
        self.fileName = fileName

        """ Pre processing class for receive data and return normalized data
    
            Attributes: fileName
    
        """
    
    def __repr__(self):
        print(self.data)
        return "Nome do Arquivo em estudo: {}".format(self.fileName)

    def load_file(self,type='txt'):
        
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
        with open(self.fileName,'r') as file:
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
        
    def save_file(self, fileType='txt'):
        
        """Function to save in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
                
        Args:
            file(string): name of a file to read from
        
        Returns:
            None
        
        """
        outPutFile = self.fileName[:-4] + "_outPut." + fileType
        with open(outPutFile,'w') as file:
            file.writelines("%s\n" % l for l in self.data)
        file.close()
           
        return print("Arquivo {} gravado com : {} dados".format(outPutFile,self.len))


def main():
    print("ditest")
    p = Preprocessor('data.txt')
    p.load_file()
    p.mean

if __name__ == 'main':
    main()