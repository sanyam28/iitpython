# finger exercise to print largest odd no, if not possible then smallest no.
def swap(array, a, b):
    newarray = []
    for i in range(len(array)):
        newarray.append(array[i])
    newarray[a] = array[b]
    newarray[b] = array[a]
    return newarray

def sort_the_list(give_array_i):
    give_array = give_array_i
    length_array = len(give_array)
    for s in range(length_array-1):
        is_swapped = False
        for i in range(length_array-1):
            if give_array[i]>give_array[i+1]:
                is_swapped=True
                give_array = swap(give_array, i, i+1)
        if is_swapped == False :
            return give_array
        is_swapped = False
    return give_array

user_input = input("Enter array elements separated by spaces: ") 
give_arrayinp = [int(x) for x in user_input.split()]
sortedarray = sort_the_list(give_arrayinp)

somi = True
for i in give_arrayinp:
    if i%2 !=0:
        somi = False
if somi:
    print("Smallest no is: "+str(sortedarray[0]))
else:
    oddno = []
    for i in range(len(give_arrayinp)):
        if give_arrayinp[i] %2 !=0:
            oddno.append(give_arrayinp[i])
    print("Largest odd no is: "+str(oddno[len(oddno)-1]))
