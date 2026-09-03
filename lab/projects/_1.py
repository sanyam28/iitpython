# Creating an algorithm to find the largest element in an array

# Lets consider an array to be sorted

array = [23,12,34,45,22,56,32,32 ,344]
def main(no_array):
    length = len(no_array)
    greatest_no = no_array[0]
    for i in range(length):
        if no_array[i]>greatest_no:
            greatest_no = no_array[i]

    return greatest_no

myno = main(array)
print(myno)