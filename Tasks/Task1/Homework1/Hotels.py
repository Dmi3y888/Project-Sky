DataBaseCars = {}
commands = ['Read', 'Enter', 'Search', 'Exit']
file_name = 'Hotels.txt'
while True:
    comand = input('Enter one of the Command from Read Base, Enter, Search: \n')
    if comand == 'Exit':
        print('Thx for visiting our base')
        break
    if comand == 'Read':
        with open(file_name, 'r') as file:
            database = file.read()
        print(database)
    elif comand == 'Enter':
        print('Enter info:\n')
        name = input('Enter name \n ')
        country = input('Enter country \n')
        city = input('Enter city \n')
        rooms = input('Enter room numbers \n')
        stars = input('Enter stars \n')
        people = input('Enter people \n')
        if not all([name, country, city, rooms, stars, people]):
            print('Error, info is not correct')
        else:
            with open(file_name, 'a') as file:
                file.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(name, country, city, rooms, stars, people))
    elif comand == 'Search':
        country = input('Searched country \n')
        with open(file_name, 'r') as file:
            stars = 0
            count_hotels = 0
            max_people = 0
            max_people_hotel = None
            for line in file:
                hotel_info = line.split('\t')
                if country == hotel_info[1]:
                    stars += int(hotel_info[4])
                    count_hotels += 1
                    if int(hotel_info[5]) > max_people:
                        max_people = int(hotel_info[5])
                        max_people_hotel = hotel_info
            if max_people_hotel is None:
                print("Hotel not found")
            else:
                print('In hotel {0} from {1} are {people} people'.format(*max_people_hotel, people=max_people))
            if count_hotels == 0:
                print("Hotels not found")
            else:
                print("Average", stars / count_hotels)
