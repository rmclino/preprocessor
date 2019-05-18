class Preprocessor():
   
    def __init__(self,):

        """ Pre processing class for receive data and return normalized data
    
            Attributes: fileName
    
        """
    
    def __rep__(self):
        return "Nome do Arquivo em estudo: {}".format(self.fileName)

    def read_dataload_file(self,fileName, outPutFile="out_put"):
        
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
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
        self.data = data_list
        self.len = len(data_list)
        return print("Arquivo com : {}".format(self.len))
    
    def mean(self):
        if self.data != None:
            self.mean = sum(data)/len(data)
        else:
            raise "No Data"
        return self.mean

if __name__ == 'main':
    p = Preprocessor()
    p.read_dataload_file('data.txt')