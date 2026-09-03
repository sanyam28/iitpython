print("I will print each letter and spaces in unique lines.")

# def main(string):
#     length = range(len(string))
#     print(length)
#     for i in length:
#         print(i)
#         print(string[i].center(i*5))

def main(string):
    for i in string:
        print(i)

userinp = input("Enter your string: ")

main(userinp)