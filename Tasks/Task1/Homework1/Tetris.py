results = {}

while True:
    tet = input('Enter name and result: \n')
    if len(tet.split()) != 2:
        break
    name, result = tet.split()
    result = int(result)
    if name in results:

        if result > results[name]:
            results[name] = result
    else:
        results[name] = result
for result in results.keys():
    print(result, results[result])