username=input("Username:")
password=input("Password:")
if(username=="mac" and password=="1234"):
    print("-"*25)
    print("welcome")
    print("1.cpu        6500")
    print("2.mainboard  2000")
    print("3.GPU        7000")
    print("4.RAM        4000")
    menu=int(input("Select the menu>>"))
    count=int(input("Select number"))
    if(menu==1):
        print("cpu price",6500*count);
    elif(menu==2):
        print("mainboard price", 2000 * count);
    elif (menu == 3):
        print("GPU price", 7000 * count);
    elif (menu == 4):
        print("RAM price", 4000 * count);
    else:
        print("please input 1-4");