# Write a code that asks the user to enter their birthday in the form mm/dd/yyyy, and then print a string othe form 
# You were born in the year yyyy

bir_inp = input("Enter your birthdate in the form mm/dd/yyyy: ")

arr = bir_inp.split('/')

print(f'You were born in the year {arr[2]}')