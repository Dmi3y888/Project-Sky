results = {}

while True:
    Country = input('Enter Country: \n')
    Citys = input('Enter City: \n')
    if Country == '' or Citys == '':
        break
    Citys = Citys.split()
    results[Country] = Citys
while True:
    searchedcity = input("Searched City ")
    for country in results.keys():
        if searchedcity in results[country]:
            print('Your Country is -', country)
