x = [[5,2,3], [10,8,9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [{'x':10, 'y':20}]
#1. Change the value 10 in x to 15 
x[1][0] = 15
print(x)

#2.Change the last_name of the first student from "Jordan" to "Bryant"
students[0]['last_name'] = 'Bryant'
print(students[0])

#3 In the sports directory change Messi to Andres
sports_directory['soccer'][0] = 'Andres'
print(sports_directory) 

#4. Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

#2b Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. 
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name' : 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterateDictionary(some_list):
    for i in range(len(students)):
        for key, val in some_list[i].items():
            print(key, '=', val,)
iterateDictionary(students)

#3b create a function iterateDictionary2(key_name,some_list) that given a list of dictionaries and a key name the function prints the value stored in tha key for each dictionary
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        for key, val in some_list[i].items():
            if key == key_name:
                print(val)
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4 Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(len(val), key)
        for i in range(0, len(val)):
            print(val[i])
printInfo(dojo)
