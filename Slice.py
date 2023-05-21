a = ["abc", "bvs", "dff", "abr", "ccd", "few", "utg", "poi"]
print(f"first 3 items are {a[0:3]}")
m = len(a) // 2
# print(a[m - 1: m + 2])
# print(a[len(a) - 3: len(a)])
b = a[0:len(a)]
a.append('chaman')
b.append('siman')

shape = {
    'circle': 'gol',
    'square': 'chaur',
    'triangle': 'trikon',
    'squar': 'chaur'
}
for sh in set(shape.values()):
    print(sh.title())

lang = {'chinese','japanese','tamil','kannad'}
print(lang)
for l in lang:
    print(l.title())

riv = {
    'Ganga':'India',
    'Nile':'Egypt',
    'Thames':'England',
    'Amazon':'America'
}


for r in riv.keys():
    print(f"River {r.title()} runs through {riv.get(r.title())}")

users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton'},
    'mcurie': {'first': 'marie','last': 'curie','location': 'paris'}
}

kid = {
    'aeinstein': ['red', 'blue','green'],
    'mcurie': ['pink','yellow','white']
}

for kid,color in kid.items():
    print(f"{kid.title()}'s favourite colours are")
    for c in color:
        print(c.title())