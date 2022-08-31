#* PROBLEM 1
def countdown(number):
    list=[]
    while number>=0:
        list.append(number)
        number -= 1
    return list



print(countdown(5))

#* PROBLEM 2
def print_and_return(list):
    print (list[0])
    return(list[1])

print(print_and_return([1,4]))



#* PROBLEM 3
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

print(first_plus_length([1,2,3,4,5]))

#* Problem 4
def greater_than_second(list):
    list2=[]
    nums=0
    if len(list) <2:
        return False
    else:
        for item in list:
            if item > list[1]:
                list2.append(item)
                nums +=1
        print(nums)
    return list2

print(greater_than_second([3]))



#* PROBLEM 5
def length_value(size, value):
    list=[]
    while size>0:
        list.append(value)
        size -= 1
    return list

print(length_value(6, 2))