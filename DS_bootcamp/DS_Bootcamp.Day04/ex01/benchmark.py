import timeit

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

def time(emails):
    times = {}
    times['it is better to use loop'] = timeit.timeit('usual_approach(emails)', globals=globals(), number=90000000)
    times['it is better to use a list comprehension'] = timeit.timeit('second_approach(emails)', globals=globals(), number=90000000)
    times['it is better to use a map'] = timeit.timeit('map_approach(emails)', globals=globals(), number=90000000)
    sorted_times = sorted(times.items(), key=lambda item: item[1])
    print(sorted_times[0][0])
    print(sorted_times[0][1], "vs", sorted_times[1][1], "vs", sorted_times[2][1])

if __name__ == '__main__':
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com',]

    time(emails)



