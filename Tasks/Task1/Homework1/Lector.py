import FileWorker


def read(name):
    print(FileWorker.read(name))


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
    data = [disciplines, number, hours, forms, name, surnames]
    if validate(data):
        FileWorker.write(file_name, data)


def search(name):
    semester = input('Searched by semester \n')
    hours = 0

    for lection_info in FileWorker.read_lines(name):

        if semester == lection_info[1]:
            hours += int(lection_info[2])
    print("All hours", hours)


def count(name):
    lectors = []

    for lector_info in FileWorker.read_lines(name):

        lector = lector_info[4] + ' ' + lector_info[5]
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
