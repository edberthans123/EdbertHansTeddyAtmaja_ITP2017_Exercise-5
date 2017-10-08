def gen(w):
    i = -1
    while w > i:
        yield w
        w -= 1

cd = gen(int(input('Insert number here: ')))
for z in cd:
    print(z)
print(type(cd))
