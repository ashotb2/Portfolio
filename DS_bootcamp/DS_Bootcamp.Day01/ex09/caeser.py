import sys

def caeser():
    if sys.argv[1].lower() == 'encode':
        shift = 12
        print(cipher(shift))
    elif sys.argv[1].lower() == 'decode':
        shift = -12
        print(cipher(shift))

    else:
        print('Invalid argument')

def cipher(s):
    input = sys.argv[2]
    result = []
    for i in range(len(input)):
            c=input[i]
            if c.isupper():
                result.append(chr((ord(c) + s-65) % 26 + 65))
            else:
                result.append(chr((ord(c) + s - 97) % 26 + 97))

    return ''.join(result)

if __name__ == '__main__':
    caeser()
