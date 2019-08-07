import csv

from PersonMethod import Person


class Patient(Person):
    _instances = []
    FILENAME = 'Patient.csv'
    columns = ['full_name', 'birth_date', 'height', 'sex', 'weight', 'diagnos']

    def __init__(self, full_name, birth_date, height, sex, weight, diagnos):
        super(Patient, self).__init__(full_name, birth_date)
        self.height = height
        self.sex = sex
        self.weight = weight
        self.diagnos = diagnos
        self._instances.append(self)

    def __str__(self):
        person = super(Patient, self).__str__()
        return person + ' Height: {}\n\n Sex: {} \n\n Weight: {} \n\n Diagnos: {} \n\n'.format(self.height, self.sex,
                                                                                               self.weight,
                                                                                               self.diagnos)

    @classmethod
    def safe_all(cls):
        with open(cls.FILENAME, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=cls.columns)
            writer.writeheader()

            writer.writerows(map(lambda user: user.dict, cls._instances))

    @classmethod
    def get_all(cls):
        with open(cls.FILENAME, "r", newline='') as file:
            reader = csv.DictReader(file)
            cls._instances = [Patient(**row) for row in reader]

    @classmethod
    def get_sum(cls):
        summa = 0
        count = 0
        for patient in cls._instances:
            if patient.sex == 'Male':
                summa += patient.height
                count += 1
        return summa / count

    @classmethod
    def get_light(cls):



    def add_patient(self):
        with open(self.FILENAME, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.columns)
            writer.writerow(self.dict)

    @property
    def dict(self):
        return {
            'full_name': self.full_name,
            'birth_date': self.birth_date,
            'height': self.height,
            'sex': self.sex,
            'weight': self.weight,
            'diagnos': self.diagnos,
        }


if __name__ == '__main__':
    s = input('type ')
    if s == 'save':
        p0 = Patient("Vas", '01-02-1991', 170, 'Male', 73, 'VRZ')
        p1 = Patient("Vis", '02-03-1992', 175, 'Male', 83, 'VRK')
        p2 = Patient("Ola", '02-03-1993', 165, 'Female', 53, 'VRN')

        Patient.safe_all()
    elif s == 'get':

        Patient.get_all()



    p3 = Patient("Gri", '02-03-1993', 165, 'Female', 53, 'VRK')
    p3.add_patient()

    print(Patient.get_sum())


    for patient in Patient._instances:

        print(patient)

