import sys

def letter():
    with open('employees.tsv', "r") as f:
        flag = False
        next(f)
        for row in f:
            n, sur, mail = row.strip().split('\t')
            if sys.argv[1] == mail:
                name = n
                flag = True
                
    if flag:
        letter = (f'Dear {name.capitalize()}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')
    else:
        letter = 'Email not found'
    return letter

if __name__ == '__main__':
    print(letter())