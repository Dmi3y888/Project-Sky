import sqlite3
from datetime import datetime

conn = sqlite3.connect("db1.sqlite")
cursor = conn.cursor()

class Person:

    def __init__(self, full_name, birth_date):
        self.full_name = full_name
        self.birth_date = birth_date
        self.id = None

    def __repr__(self):
        return 'Full name of person is: {}, and the birth date is: {}'.format(self.full_name, self.birth_date)

    def __str__(self):
        return 'Full name of person is: {}\n\n The birth date is: {}\n\n'.format(self.full_name, self.birth_date)

    def calculate_years(self):
        return datetime.now().year - datetime.strptime(self.birth_date, '%d-%m-%Y').year

    def update(self):
        sql_update = '''
        UPDATE person 
        SET birth_date = "{birth_date}", full_name = "{full_name}"
        WHERE id = "{id}" '''

        cursor.execute(sql_update.format(**self.dict))
        conn.commit()
    def insert(self):

        sql_insert = '''insert into person (full_name, `birth_date`)  
                     values ('{full_name}', '{birth_date}')'''

        cursor.execute(sql_insert.format(**self.dict))
        conn.commit()
        pk = cursor.lastrowid
        self.id = pk

    @property
    def dict(self):
        return {
            'full_name': self.full_name,
            'birth_date': self.birth_date,
            'id': self.id
            }

if __name__ == '__main__':
    saha = Person('Poraiko Oleksandr Viorelovuch', '28-06-1993')
    petka = Person('Poroshenko Petro Batkovuch', '13-02-1775')
    dashka = Person('Ivanova Dasha Ivanovna', '1-01-1992')

    TablePerson = """CREATE TABLE `person` (
          `id`  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
          `full_name` Varchar(256)  NOT NULL,
          `birth_date` DATETIME NOT NULL
        );"""
    # cursor.execute(TablePerson)
    # conn.commit()
    saha.insert()
    petka.insert()
    dashka.insert()
    dashka.full_name = 'Mashka'
    dashka.update()
    conn.close()

# SELECT * FROM person WHERE full_name like "%po%"

# SELECT avg (date('now')-birth_date) FROM person

# UPDATE person
# SET birth_date = '1975-02-01' WHERE id=2

# SELECT full_name from person WHERE birth_date BETWEEN "1980-01-01" AND "1995-01-01"

# SELECT full_name, birth_date FROM person ORDER by birth_date DESC

# SELECT full_name, birth_date FROM person ORDER by birth_date

# SELECT full_name, birth_date FROM person
# WHERE id in (1,2)
# or birth_date>'1976-01-01'

