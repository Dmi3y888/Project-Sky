from PersonMethod import Person
import sqlite3
import datetime
# class PersonDB(Person):

if __name__ == '__main__':
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    # TablePerson = """CREATE TABLE `Person` (
    #       `id`  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
    #       `full_name` Varchar(256)  NOT NULL,
    #       `birth_date` DATETIME NOT NULL
    #     );"""

    humans_lst = [('Poraiko Oleksandr Viorelovuch',	'28-06-1993'),('Poroshenko Petro Batkovuch','13-02-1975')]
    sql_insert = "insert into person`(`full_name, `birth_date`) " \
                 "values ({full_name}, {birth_date})"
    for raw_human in humans_lst:
        full_name = raw_human[0]
        birth_date = datetime.datetime.strptime(raw_human[1], '%Y-%m-%d').strftime()
    conn.commit()
    conn.close()

