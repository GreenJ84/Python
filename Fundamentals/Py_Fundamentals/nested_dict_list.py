
#*PROBLEM 1
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

    # *1
x[1][0]=15
# print(x)
    # *2
students[0]['last_name']='Bryant'
# print(students)
    # *3
sports_directory['soccer'][0]='Andres'
# print(sports_directory)
    # *4
z[0]['y']=30
# print(z)




#* PROBLEM 2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(list):
    for item in list:
        key_value= ''
        for name_key in item:
            # print(name_key)
            key_value += (name_key + ' - ')
            key_value += (item[name_key] +', ')
        print(key_value)

iterateDictionary(students)




# #* PROBLEM 3
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_name, list):
    for item in list:
        x = item.get(key_name)
        print(x)

iterateDictionary2('last_name', students) 








#* PROBLEM 4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for item in dict:
        print(f'{len(dict[item])} {item}')
        for i in dict[item]:
            print(i)
        print('')

printInfo(dojo)




