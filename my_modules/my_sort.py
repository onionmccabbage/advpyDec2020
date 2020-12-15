# we can sort the members of a non-ordinal collection, such as a dict, set etc.
salaries = dict(Jo=23000,Bo=19500,Flo=23000,Dave=23000,Mike=42000,Jane=42000, Tom=23000)

# we CAN impose an order by sorting the collection
name_keys = sorted(salaries.keys())
salary_keys = sorted(salaries.keys(), key= lambda key: salaries[key]) # this accesses the values
# sort by name and salary
salary_and_name_keys = sorted(salaries.keys(), key = lambda key: (salaries[key], key))

for n in name_keys:
    print(f'{n} earns { salaries[n] }')

for n in salary_keys:
    print(f'{n} earns { salaries[n] }')

for n in salary_and_name_keys:
    print(f'{n} earns { salaries[n] }')