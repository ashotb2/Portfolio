import timeit
import random
from collections import Counter

def dic(data):
    count_dict = {}
    for i in data:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict

def dic_counter(data):
    return dict(Counter(data))

def top10(data):
    d = dic(data)
    sorted_dic = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return sorted_dic[:10]

def top10_counter(data):
    d = Counter(data)
    return d.most_common(10)



if __name__ == '__main__':
    gen = [random.randint(0,100) for _ in range(1000000)]
    func_time = timeit.timeit('dic(gen)', globals=globals(), number = 1)
    count_time = timeit.timeit('dic_counter(gen)', globals=globals(), number = 1)
    top10_time = timeit.timeit('top10(gen)', globals=globals(), number = 1)
    top10_count_time = timeit.timeit('top10_counter(gen)', globals=globals(), number = 1)
    print('my function:',func_time)
    print('Counter:',count_time)
    print('my top:',top10_time)
    print("Counter's top:",top10_count_time)