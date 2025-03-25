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

def time(emails):
    usual_time = timeit.timeit('usual_approach(emails)', globals=globals(), number=90000000)
    second_time = timeit.timeit('second_approach(emails)', globals=globals(), number=90000000)
    if second_time < usual_time:
        print('it is better to use a list comprehension')
        print(second_time, "vs",usual_time)
    else:
        print('it is better to use a loop')
        print(usual_time, "vs", second_time)

if __name__ == '__main__':
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com',]
    
    time(emails)



