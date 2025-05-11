
print("......food manu.......")

print("1.food\n2.drink\n3.Exit")

choice=input("enter your choice:")

if choice=='1':
    print("....food manu....\nA.\tbanina\nB.\trice\nC.\tapple")
    food_choice=input("enter your food:")
    if food_choice=="A":
        print("banina")
    elif food_choice=="B":
        print("rice")
    elif food_choice=="c":
        print("apple")
    else:
        print("not found")

elif choice=="2":
    print("...drink manu...\nA.\tcoffe\nB.\ttea\nC.mojo")
    drink_choice=input("enter your choice:")
    if drink_choice=="A":
        print("coffe")
    elif drink_choice=="B":
        print("tea")
    elif drink_choice=="C":
        print("mojo")
elif choice=="3":
    print("thank you! good bye")




