from PersonMethod import Person


class Student(Person):
    _instances = []

    def __init__(self, full_name, birth_date, fak, group, payments, mark):
        super(Student, self).__init__(full_name, birth_date)
        self.fak = fak
        self.group = group
        self.payments = float(payments)
        self.mark = mark
        self._instances.append(self)

    def __str__(self):
        person = super(Student, self).__str__()
        return person + ' Fak: {}\n\n Group: {} \n\n Pay: {} \n\n Mark: {} \n\n'.format(self.fak, self.group,
                                                                                        self.payments, self.mark)

    @classmethod
    def get_student_by_group(cls, group):
        return list(filter(lambda student: student.group == group, cls._instances))

    @classmethod
    def get_pay(cls, group):
        pay = 0
        for student in cls.get_student_by_group(group):
            pay += student.payments
        return pay

    @classmethod
    def get_yers(cls, group):
        summa = 0
        count = 0
        for student in cls.get_student_by_group(group):
            summa += student.calculate_years()
            count += 1
        return summa / count


if __name__ == '__main__':
    st = Student('Vadim Prim', '23-11-1994', 'FisMath', '33', '1000', '9')
    st1 = Student('Vas Vas', '22-01-1995', 'Math', '33', '1100', '8')
    st2 = Student('Per Per', '21-01-1996', 'Math', '33', '1200', '7')
    st3 = Student('Mas Mas', '20-01-1997', 'Math', '34', '1300', '8')
    # print(st, st1, st2, st3)
    print(Student.get_pay('33'), Student.get_yers('33'), Student.get_student_by_group('34'))
