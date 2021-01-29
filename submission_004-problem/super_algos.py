
def find_min(element):
    """TODO: complete for Step 1"""
    for i in element:
        if type(i) == str:
            return -1 
    if len(element) == 0:  
        return -1
    elif len(element) == 1:
        return element[0]
    else:
        v = find_min(element[1:])
        if v < element[0]:
            return v
        else:
            return element[0]

my_list = [3,6,8,9,3,11]
print (find_min(my_list)) 


def sum_all(element):
    """TODO: complete for Step 2"""

    for i in element:
        if type(i) == str:
            return -1 
    if len(element) == 0:  
        return -1
    elif len(element) == 1:
        return element[0]
    else:
        return element[0] + sum_all(element[1:])
my_list = [1,2,3,4,5]
print (sum_all(my_list)) 


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    new_list = []
    for z in character_set:
        if type(z) != str:
            return new_list
    if n == 1:
        return(character_set)
    else:
        for i in character_set:
            for x in find_possible_strings(character_set, n - 1):
                new_list.append(i+x)
        return new_list

character_set = ["x","y"]
k = 2
print(find_possible_strings(character_set, k))