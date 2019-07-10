results = {}

while True:
    president = input('Name of President Value: \n')
    if len(president.split()) != 2:
        break
    name, value = president.split()
    if name in results:
        results[name] += int(value)
    else:
        results[name] = int(value)
for result in results.keys():
    print(result, results[result])
