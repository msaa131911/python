
user_name="admin"
usr_pwd="10000"

input_user=input("enter your user name:")
input_pwd=input("enter your password:")

if input_user==user_name and input_pwd==usr_pwd:
    print("good")

elif input_user!=user_name and input_pwd != usr_pwd:
    print("wrong")

else:
    print(".............@@@@@")