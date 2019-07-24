def read(name):
    with open(name, 'r') as file:
        database = file.read()
    print(database)

def validate(data):

    if data[0] not in ["Exam", 'Offset']:
        print('Error, enter correct info - Exam or Offset')
        return False

    if not all(data):
        print('Error, info is not correct')
        return False
    return True

def enter(file_name):

    print('Enter info:\n')
    disciplines = input('Enter disciplines \n ')
    number = input('Enter number of semester \n')
    hours = input('Enter hours in semester \n')
    forms = input('Enter Exam or Offset \n')
    name = input('Enter name \n')
    surnames = input('Enter surnames \n')
    if validate([forms, disciplines, number, hours, name, surnames]):
        with open(file_name, 'a') as file:
            file.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(disciplines, number, hours, forms, name, surnames))


def search(name):
    semester = input('Searched by semester \n')
    with open(name, 'r') as file:
        hours = 0

        for line in file:
            lection_info = line.split('\t')
            if semester == lection_info[1]:
                hours += int(lection_info[2])
        print("All hours", hours)

def count(name):
    with open(name, 'r') as file:
        lectors = []

        for line in file:
            lector_info = line.split('\t')
            lector = lector_info[4]+' '+lector_info[5]
            if lector not in lectors:
                lectors.append(lector)
        print('Unique Lektors', lectors)

def run():
    DataBase = {}
    commands = ['Read', 'Enter', 'Search', 'Exit']
    file_name = 'Lektors.txt'


    while True:
        comand = input('Enter one of the Command from Read Base, Enter, Search: \n')
        if comand == 'Exit':
            print('Thx for visiting our base')
            break

        if comand == 'Read':
            read(file_name)

        elif comand == 'Enter':
            enter(file_name)

        elif comand == 'Search':
            search(file_name)

        elif comand == 'Count':
            count(file_name)

if __name__ == "__main__":
    run()
