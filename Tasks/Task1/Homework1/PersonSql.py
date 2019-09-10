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
class Patient(Person):

    def __init__(self, full_name, birth_date, height, sex, weight, diagnos, id=None, person_id=None):
        super(Patient, self).__init__(full_name, birth_date)
        self.height = height
        self.sex = sex
        self.weight = weight
        self.diagnos = diagnos
        self.person_id = person_id
        self.id = id


    def __str__(self):
        person = super(Patient, self).__str__()
        return person + ' Height: {}\n\n Sex: {} \n\n Weight: {} \n\n Diagnos: {} \n\n'.format(self.height, self.sex,
                                                                                               self.weight,
                                                                                               self.diagnos)


    @property
    def dict(self):
        return {
            'full_name': self.full_name,
            'birth_date': self.birth_date,
            'height': self.height,
            'sex': self.sex,
            'weight': self.weight,
            'diagnos': self.diagnos,
            'id': self.id,
            'person_id': self.person_id
        }

    def insert(self):

        person_insert = '''insert into person (full_name, `birth_date`)  
                     values ('{full_name}', '{birth_date}')'''

        cursor.execute(person_insert.format(**self.dict))
        conn.commit()
        pk = cursor.lastrowid
        self.person_id = pk

        patient_insert = '''insert into patient (height, sex, weight, diagnos, person_id)  
                             values ('{height}', '{sex}','{weight}','{diagnos}','{person_id}')'''

        cursor.execute(patient_insert.format(**self.dict))
        conn.commit()
        pk = cursor.lastrowid
        self.id = pk

    def update(self):

        person_update = '''
           UPDATE person 
           SET birth_date = "{birth_date}", full_name = "{full_name}"
           WHERE id = "{person_id}" '''

        cursor.execute(person_update.format(**self.dict))
        patient_update = '''
            UPDATE patient 
            SET sex = "{sex}"
            WHERE id = "{id}" '''

        cursor.execute(patient_update.format(**self.dict))
        conn.commit()

    @staticmethod
    def get_by_id(id):

        person_select = '''
            SELECT person.full_name, person.birth_date, 
            height, sex, weight, diagnos,  patient.id, person_id
            FROM patient 
            INNER JOIN person ON person.id = patient.person_id
            WHERE patient.id = {id}
        '''

        cursor.execute(person_select.format(id=id))

        pat = cursor.fetchone()
        conn.commit()
        print(pat)

        return Patient(*pat)


if __name__ == '__main__':
    saha = Patient('Poraiko Oleksandr Viorelovuch', '28-06-1993', 175, 'man', 65, "pkl")
    petka = Patient('Poroshenko Petro Batkovuch', '13-02-1775', 185, 'man', 75, "wkl")
    dashka = Patient('Ivanova Dasha Ivanovna', '1-01-1992', 165, 'women', 55, "pkl")

    TablePerson = """CREATE TABLE `patient` (
          `id`  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
          `height` Float NOT NULL,
          `sex` Varchar NOT NULL,
          `weight` Float NOT NULL,
          `diagnos` Varchar NOT NULL,
          `person_id` Integer NOT NULL
                  );"""

    # cursor.execute(TablePerson)
    # conn.commit()
    # saha.insert()
    # petka.insert()
    # dashka.insert()
    pat_2 = Patient.get_by_id(2)
    print(pat_2)
    pat_2.sex = 'women'
    pat_2.update()
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

