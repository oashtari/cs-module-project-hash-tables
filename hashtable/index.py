records = [
    ('Alice', 'Engineering'),
    ('Bob', 'Sales'),
    ('Carol', 'Sales'),
    ('Dave', 'Engineering'),
    ('Erin', 'Engineering'),
    ('Frank', 'Engineering'),
    ('Grace', 'Marketing')
]

# who works in each department

dept = 'Engineering'

dept_idx = {}

def add_dept_idx(name, dept):
    if dept not in dept_idx:
        dept_idx[dept] = []
    
    dept_idx[dept].append(name)

for name, dept in records:
    add_dept_idx(name, dept)

print(dept_idx)

# clearly need to make a better (helper) function so we're not repeating data below

records.append(('Beej', 'Engineering')) #updating the main database
add_dept_idx('Beej', 'Engineering') #updating the index which was created to speed up queries

#slow code
# for r in records:    # O(n)
#     if r[1] = dept:
# print(r[0])

# what is the key? -- dept
# what is the value? -- list of names
