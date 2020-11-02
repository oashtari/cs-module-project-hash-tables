
d = {
    'foo': 12,
    'bar': 17, 
    'qux': 2
}

items = list(d.items())

# sort by key
items.sort()

for i in items:
    print(f'{i[0]}: {i[1]}')

# sort by value (sorting by 2nd item in tuple)

"""
def sort_by(t):
    return t[1]

items.sort(key=sort_by)
"""
# this does the same as commented out code above
# lambda means it is an anonymous function, takes parameter t and returns t[1] 
# sort can also take another keyword parameter of 'reverse'
items.sort(key=lambda t: t[1], reverse=True)

for i in items:
    print(f'{i[0]}: {i[1]}')




# .items() returns an interator
# list(d.items()) turns it into a list
# assign to variable: x = list(d.items())
# sort it sorted(x), will auto sort based on key, then value if same key

