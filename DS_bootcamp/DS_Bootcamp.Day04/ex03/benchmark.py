import timeit
import sys
from functools import reduce

def loop_approach(data):
    sum = 0
    for i in range(data+1):
        sum = sum + i * i
    return sum

def reduce_approach(data):
    sum = reduce(lambda total, i: total + i * i, range(data+1), 0)
    return sum


if __name__ == '__main__':
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com',]
    
    
    if len(sys.argv) == 4:
        method = sys.argv[1]
        iter = int(sys.argv[2])
        num = int(sys.argv[3])
        
        if method == 'loop':
            print(timeit.timeit('loop_approach(num)', globals=globals(), number=iter))
        elif method == 'reduce':
            print(timeit.timeit('reduce_approach(num)', globals=globals(), number=iter))


