class Mydict(dict):
    def get(self, key, default=0):
        return dict.get(self, key, default)


a = {
    'a': 1, 'b': 2
}

b = Mydict(a=1, b=2)

print(a, b)
print(a.get('12'))
print(b.get('13'))
