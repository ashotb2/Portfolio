def main():
    class Must_read:
        with open('data.csv', "r") as f:
            print(f.read())

if __name__ == '__main__':
    main()