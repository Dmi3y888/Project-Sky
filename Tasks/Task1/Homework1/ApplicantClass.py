import csv
import shelve

from PersonMethod import Person


class Applicant (Person):
    _instances = []
    FILENAME = 'Applicant.csv'
    FILENAME_SHELVE = 'Applicant'
    columns = ['full_name', 'birth_date', 'fak', 'spec', 'sred']

    def __init__(self, full_name, birth_date, fak, spec, sred):
        super(Applicant, self).__init__(full_name, birth_date)
        self.fak = fak  # факультет
        self.spec = spec  # посада
        self.sred = sred  # средний бал
        self._instances.append(self)

    @classmethod
    def export_to_csv(cls):
        with open(cls.FILENAME, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=cls.columns)
            writer.writeheader()

            writer.writerows(map(lambda user: user.dict, cls._instances))

    @classmethod
    def import_from_csv(cls):
        with open(cls.FILENAME, "r", newline='') as file:
            reader = csv.DictReader(file)
            cls._instances = [Applicant(**row) for row in reader]

    @property
    def dict(self):
        return {
                   'full_name': self.full_name,
                   'birth_date': self.birth_date,
                    'fak': self.fak,
                    'spec' : self.spec,
                    'sred' : self.sred
        }

    @classmethod
    def export_to_shelve(cls):
        with shelve.open(cls.FILENAME_SHELVE, "n") as applicants:
            for applicant in cls._instances:
                applicants[applicant.full_name] = applicant

    @classmethod
    def import_from_shelve(cls):
        with shelve.open(cls.FILENAME_SHELVE, "r") as applicants:
            cls._instances = list(applicants.values())

    @classmethod
    def find_from_shelve(cls, full_name):
        with shelve.open(cls.FILENAME_SHELVE) as applicants:
            return applicants.get(full_name, "Not Found")

    def add_shelve(self):
        with shelve.open(self.FILENAME_SHELVE) as applicants:
            applicants[self.full_name] = self


if __name__ == '__main__':

    p0 = Applicant("Vas", '22-01-1995', 'Math', 'Spec', 133)
    p1 = Applicant("Vis", '02-03-1992', 'Math', 'Spec', 173)

    Applicant.export_to_shelve()
    Applicant.import_from_shelve()
    print(Applicant._instances)

    Applicant.export_to_csv()
    Applicant.import_from_csv()

    print(Applicant._instances)

    p2 = Applicant("Ola", '02-03-1993', 'Math', 'Spec', 143)
    p2.add_shelve()

    print(Applicant._instances)

    print(Applicant.find_from_shelve("Vas"))
    print(Applicant.find_from_shelve("Vls"))