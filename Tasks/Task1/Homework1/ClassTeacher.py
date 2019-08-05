from PersonMethod import Person


class Teacher(Person):
    _instances = []

    def __init__(self, full_name, birth_date, fak, pos, pro, pay, kur):
        super(Teacher, self).__init__(full_name, birth_date)
        self.fak = fak  # факультет
        self.pos = pos  # посада
        self.pro = pro  # вчене звання
        self.pay = pay  # зарплата
        self.kur = kur  # количество курсов
        self._instances.append(self)

        def __str__(self):
            person = super(Teacher, self).__str__()
            return person + ' Fak: {}\n\n Pos: {} \n\n Pro: {} \n\n Pay: {} \n\n Kur: {} \n\n '.format(self.fak,
                                                                                                       self.pos,
                                                                                                       self.pro,
                                                                                                       self.pay,
                                                                                                       self.kur)

