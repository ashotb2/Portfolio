def read():
    f = open("/home/ashot/Documents/School21/ds.csv", "r")
    lines = f.readlines()
    f.close()
    
    f=open("/home/ashot/Documents/School21/DS_Bootcamp.Day01-1/ex01/ds.tsv", "a")
    mod_lines = []
    for line in lines:
        count = 0
        mod_line = ""
        for c in range(len(line)):
            if line[c] == '\"':
                count += 1
            if line[c] == ',' and count % 2 == 0:
                mod_line += '\t'
            else:
                mod_line += line[c]
        f.write(mod_line)
    f.close()

if __name__ == '__main__':
    read()