#pase/fail


Reg=int(input("enter your registration number:"))
roll=int(input("enter your roll number:"))

mark=int(input("enter your mark:"))


if mark>=90:
    print("gold A+")

elif mark>=80:
    print("A+")

elif mark>=70:
    print("A")

elif mark>=60:
    print("A-")

elif mark>=50:
    print("B")

elif mark>=40:
    print("C")

elif mark>=33:
    print("D")

else:
    print("fail")




