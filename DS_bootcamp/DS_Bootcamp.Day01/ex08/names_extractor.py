import sys

def main():
    input = sys.argv[1]
    table = []
    with open(input, "r") as f:
        emails = f.readlines()
    
    for email in emails:
        name, domain, com = email.strip().split('.')
        surname, domain = domain.split('@')
        table.append([name, surname, email])
    
    with open('employees.tsv', "w") as f:
        f.write('Name\tSurname\tE-mail\n')
        for row in table:
            f.write(row[0]+'\t'+row[1]+'\t'+row[2])

if __name__ == '__main__':
    main()