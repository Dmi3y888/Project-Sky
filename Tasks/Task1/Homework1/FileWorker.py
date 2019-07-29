def read(name):
    with open(name, 'r') as file:
        return file.read()


def write(file_name, data):
    with open(file_name, 'a') as file:
        file.write('\t'.join(map(str, data)) + '\n')


def read_lines(name):
    with open(name, 'r') as file:
        return [line.split('\t') for line in file]
