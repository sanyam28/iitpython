# to get srray sorted in an ascending order
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
            print("iterations",(s+1)*(i+1))
            return give_array
        is_swapped = False
    return give_array

user_input = input("Enter array elements separated by spaces: ") 
give_arrayinp = [int(x) for x in user_input.split()]
sortedarray = sort_the_list(give_arrayinp)
print('The sorted array is: ')
print(sortedarray)
# operators = ['=', '<']
def putoperators(arr):
    newarr = []
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            try:
                if arr[i] == newarr[2*i] :
                    newarr.append('<')
                    newarr.append(arr[i+1])
                else:
                    newarr.append(arr[i])
                    newarr.append('<')
                    newarr.append(arr[i+1])

            except:
                newarr.append(arr[i])
                newarr.append('<')
                newarr.append(arr[i+1])

        else:
            try:
                if arr[i] == newarr[2*i]:
                    newarr.append('=')
                    newarr.append(arr[i+1])

                else:
                    newarr.append(arr[i])
                    newarr.append('=')
                    newarr.append(arr[i+1])
            except:
                newarr.append(arr[i])
                newarr.append('=')
                newarr.append(arr[i+1])

    return newarr

oper_arr = putoperators(sortedarray)
# print(*oper_arr)
for x in range(len(oper_arr)):
    if x == len(oper_arr) -1:
        print(oper_arr[x])
    else:
        print(oper_arr[x], end="")
