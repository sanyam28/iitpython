# Writing a code to get absolute value of a number

# def mod(no):
#     if no>=0:
#         return no
#     else:
#         temp = no*2
#         modno = no - temp
#         return modno

# user_no = int(input("Choose your number ti get absolute value of it: "))
# resp = mod(user_no)
# print(resp)
user_no = int(input("Choose your number ti get absolute value of it: "))
if user_no>=0:
    print(user_no)
else:
    print(user_no*-1)