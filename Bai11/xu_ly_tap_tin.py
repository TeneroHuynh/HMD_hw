def read_file(filename):
    f = open(filename, 'r')
    content = f.read()
    print(content)
    f.close()
