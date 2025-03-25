def data_types():
    my_int = 10
    my_str = "Hello"
    my_float = 10.5
    my_bool = True
    my_list = [1, 2, 3]
    my_dict = {"key": "value"}
    my_tuple = (1, 2, 3)
    my_set = {1, 2, 3}

    types = [type(my_int), type(my_str), type(my_float), type(my_bool), type(my_list), type(my_dict), type(my_tuple), type(my_set)]
    print([t.__name__ for t in types])

if __name__ == '__main__':
    data_types()