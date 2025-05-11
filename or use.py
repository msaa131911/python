sum1 = 10
sum2 = 20
sum3 = 30

roll = input("Enter roll no: ")  # Input is a string
ss = "asa"
nn = "ny"
dd = "jy"


if (sum2 > sum1 and sum1 < sum2) or (sum3 > sum2):
    if roll == "4141":
        print(ss)

elif sum3 > sum1 and sum1 < sum3:
    if roll == "4242":
        print(nn)

elif sum1 < sum2:
    if roll == "4343":  
        print(ss)

else:
    print("Not working")
