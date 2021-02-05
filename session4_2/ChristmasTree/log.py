class FileLog():
    __instance = None
    @staticmethod
    def getInstance():
        """Static Access Method"""
        if FileLog.__instance == None:
            Filelog()
        return Filelog.__instance
    def __init__(self):
        """Virtually Private Constructor"""
        if FileLog.__instance != None:
            FileLog.__instance
        else:
            FileLog.__instance = self
        self.file = open("logger.txt", "a")

    def info(self, msg):
        self.file.write("info: " + msg +"\n" )

    def warning(self, msg):
        self.file.write("Warning: " + msg + "\n")

    def error(self, msg):
        self.file.write("Error: " + msg + "\n")


'''
The following function serves as a simple test to check
whether the id of multiple instances of Filelog remain
the same.
'''

def FileLogTest(filelogInstance = None):
    if filelogInstance == None:
        raise ValueError('Filelog Instance doesn\'t exist')

    log = filelogInstance()
    log.warning('One CS162 Filelog instance found with id ' + str(id(log)))
    log2 = filelogInstance().getInstance()
    log2.warning('Another CS162 Filelog instance Found with id ' + str(id(log2)))

FileLogTest(filelogInstance = FileLog)