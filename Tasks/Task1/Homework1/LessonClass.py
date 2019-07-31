class FootballClub:

    def get_name(self):
        return self.name

    def __init__(self, name, country, year, president, budget=0, trophy_count=0):
        self.name = name
        self.country = country
        self.year = year
        self.president = president
        self.budget = budget
        self.trophy_count = trophy_count

    def __str__(self):
        return 'Name: {0}\nOther info:\n{1}, {2}, {3}, {4}.\nTrophies - {5}\n'.format(self.name, self.country,
                                                                                      self.year, self.president,
                                                                                      self.budget, self.trophy_count)

    def __add__(self, other):
        club = FootballClub(self.name + ' ' + other.name, self.country, 2019, self.president,
                            self.budget + other.budget, self.trophy_count + other.trophy_count)
        self.deleted = True
        other.deleted = True

        return club

    def __eq__(self, other):
        return self.name == other.name and self.country == other.country


chelsie = FootballClub('Chelsie', 'England', 1908, 'Abramovich', 100000000, 13)
madrid = FootballClub('Real Madrid', "Spain", 1876, 'Peres', trophy_count=102)
newchelsie = FootballClub('Chelsie', 'England', 1908, 'Abramovich', 100000000, 13)

print(chelsie)
print(madrid)

print(chelsie + madrid)
print(madrid + chelsie)

print(chelsie == newchelsie)

if chelsie == newchelsie:
    print('eq')
else:
    print('no')
