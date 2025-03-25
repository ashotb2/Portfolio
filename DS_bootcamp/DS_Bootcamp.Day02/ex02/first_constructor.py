import sys
import os

class Research:
    def __init__(self):
        file=sys.argv[1]
        if os.path.isfile(file):
            print(self.file_reader(file))
        else:
            raise Exception('File path does not exist')
    
    def file_reader(self, file):
        with open(file, "r") as f:
            return f.read()

if __name__ == '__main__':
    try:
        Research()
    except Exception as e:
        print(e)