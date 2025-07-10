def unique_numbers(numbers):
    sum=0
    for n in numbers:
        sum += n
    #print(sum)
    unique=sorted(set(numbers))
    unique_sum=0
    for n in unique:
        unique_sum += n
    #print(unique_sum)
    difference_sum=sum-unique_sum
    #print(difference_sum)
    if difference_sum % 2 == 0 :
        return numbers
    else:
        return unique

print(unique_numbers([1,3,2,2]))