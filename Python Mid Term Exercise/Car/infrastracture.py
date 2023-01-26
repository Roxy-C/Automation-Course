import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class Infrastracture:        
    def log(self, message):
        try:
            time = datetime.now().strftime(" %d/%m/%Y %H:%M:%S ")
            os.chdir(os.getenv('LOGLOCATION'))
            self.file = open(os.getenv('LOGNAME'), 'a')
            self.file.write(message + "\t" + time + "\n")
            self.file.flush()
            self.file.close()
        except FileNotFoundError:
            print("Exception occurred: File not found")