from datetime import datetime
import FileWorker


class Person:
    file = 'Humans.txt'

    def __init__(self, full_name, birth_date):
        self.full_name = full_name
        self.birth_date = birth_date

    def __repr__(self):
        return 'Full name of person is: {}, and the birth date is: {}'.format(self.full_name, self.birth_date)

    def __str__(self):
        return 'Full name of person is: {}\n\n The birth date is: {}\n\n'.format(self.full_name, self.birth_date)

    def save_human(self):
        FileWorker.write(self.file, [self.full_name, self.birth_date])

    def get_humans(self):
        return FileWorker.read(self.file)

    def calculate_years(self):
        return datetime.now().year - datetime.strptime(self.birth_date, '%d-%m-%Y').year


if __name__ == '__main__':
    saha = Person('Poraiko Oleksandr Viorelovuch', '28-06-1993')
    saha.save_human()
    petka = Person('Poroshenko Petro Batkovuch', '13-02-1775')
    petka.save_human()
    dashka = Person('Ivanova Dasha Ivanovna', '1-01-1992')
    dashka.save_human()
    dashka.calculate_years()
    print(petka.get_humans())
    print(saha.calculate_years())
    print(petka.calculate_years())
    print(dashka.calculate_years())
