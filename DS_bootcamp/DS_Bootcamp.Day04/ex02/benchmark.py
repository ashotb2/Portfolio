import timeit
import sys

def usual_approach(data):
    gmail = []
    for email in data:
        if '@gmail.com' in email:
            gmail.append(email)

    return gmail

def second_approach(data):
    gmail =[email for email in data if '@gmail.com' in email]
    return gmail

def map_approach(data):
    def func(email):
        if '@gmail.com' in email:
            return email
    
    m = map(func, data)
    return m

def filter_approach(data):
    def func(email):
        if '@gmail.com' in email:
            return email
    
    m = filter(func, data)
    return m


if __name__ == '__main__':
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com',]
    
    
    if len(sys.argv) == 3:
        method = sys.argv[1]
        num = int(sys.argv[2])
        
        if method == 'loop':
            print(timeit.timeit('usual_approach(emails)', globals=globals(), number=num))
        elif method == 'list_comprehension':
            print(timeit.timeit('second_approach(emails)', globals=globals(), number=num))
        elif method == 'map':
            print(timeit.timeit('map_approach(emails)', globals=globals(), number=num))
        elif method == 'filter':
            print(timeit.timeit('filter_approach(emails)', globals=globals(), number=num))

