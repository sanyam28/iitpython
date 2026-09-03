print("I will print 5th letter of your string. spaces will be be considered.")

def main(string):
    if len(string)<5:
        print("Minimum character limit is 5")
        return
    print(string[4])

userinp = input("Enter your sring: ")

main(userinp)

print("Thank You".center(100,'-'))