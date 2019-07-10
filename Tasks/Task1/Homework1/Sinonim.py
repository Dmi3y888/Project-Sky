slk = {'Hello': 'Hi',
       'Bye': 'Goodbye',
       'List': 'Array'
       }
while True:
    sw = input('Your word ')
    if sw == '':
        break
    for name, value in slk.items():
        if sw == name:
            print(value)
        if sw == value:
            print(name)