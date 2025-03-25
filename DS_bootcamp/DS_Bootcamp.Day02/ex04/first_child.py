import sys
import os
from random import randint

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
        def __init__(self, data):
            self.data = data

        def counts(content):
            heads = sum(row[0] for row in content)
            tails = sum(row[1] for row in content)
            return heads, tails
            
        def fractions(heads, tails):
            total = heads + tails
            headratio = heads/total*100
            tailsratio = tails/total*100
            return(headratio, tailsratio)
        
class Analytics(Research.Calculations):
    def predict_random(self, num_predict):
        pred = []
        for _ in range(num_predict):
            rand = randint(0,1)
            pred.append([rand, 1 - rand])
        return pred

    
    def predict_last(self):
        return self.data[-1]

if __name__ == '__main__':
    try:
        print(Research().data)
        counts = Research.Calculations.counts(Research().data)
        print(*counts)
        print(*Research.Calculations.fractions(*counts))
        print(Analytics(Research().data).predict_random(3))
        print(Analytics(Research().data).predict_last())
    except Exception as e:
        print(e)