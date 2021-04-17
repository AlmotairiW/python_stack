x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = 'Bryant'
print(students[0]["last_name"])
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = 'Andres'
print(sports_directory["soccer"][0])
# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for idx in range(0,len(students)):
            print(f" first_name - {students[idx]['first_name']}, last_name - {students[idx]['last_name']}")
iterateDictionary(students)

#Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for idx in range(0,len(some_list)):
        print(some_list[idx][key_name])
iterateDictionary2('last_name', students)

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated values within each key's list
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    print(len(dojo['locations']), " LOCATIONS")
    for idx in range(0,len(dojo['locations'])):
        print(dojo['locations'][idx])
    print(len(dojo['instructors']), " INSTRUCTORS")
    for idx in range(0,len(dojo['instructors'])):
        print(dojo['instructors'][idx])
printInfo(dojo)