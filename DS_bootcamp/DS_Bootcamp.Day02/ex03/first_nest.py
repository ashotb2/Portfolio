import sys
import os

class Research:
    def __init__(self):
        file = sys.argv[1]
        if os.path.isfile(file):
            self.data = self.file_reader(file)
        else:
            raise Exception('File path does not exist')
    
    def file_reader(self, file, has_header=True):
        with open(file, "r") as f:
            lines = f.readlines()
            if all(cell.isalpha() for cell in lines[0].strip().split(',')):
                lines = lines[1:]
            content = [list(map(int, line.strip().split(','))) for line in lines]
            return content
    
    class Calculations:
        def counts(content):
            heads = sum(row[0] for row in content)
            tails = sum(row[1] for row in content)
            print(heads, tails)
            return heads, tails
            

        def fractions(heads, tails):
            total = heads + tails
            headratio = heads/total*100
            tailsratio = tails/total*100
            print(headratio, tailsratio)

if __name__ == '__main__':
    try:
        print(Research().data)
        counts = Research.Calculations.counts(Research().data)
        Research.Calculations.fractions(*counts)
    except Exception as e:
        print(e)