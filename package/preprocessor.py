class Preprocessor():
    """ Pre processing class for receive data and return normalized data
    
    Attributes: fileName
    
    """
    def __init__(self,fileName, outPutFile="out_put"):
        self.fileName = fileName
    
    def __rep__(self):
        return "Nome do Arquivo em estudo: {}".format(self.fileName)