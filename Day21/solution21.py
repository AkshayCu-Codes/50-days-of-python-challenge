def make_tuples(list1,list2):
    while(len(list1)==len(list2)):
        tuples=zip(list1,list2)
        return list(tuple(tuples))
    return 'Enter list of same size'
print(make_tuples([1,2,3,4],[5,6,7,8]))
print('---------------------------------')
print(make_tuples([2,3,4],[7,8]))
