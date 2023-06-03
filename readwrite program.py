def read():
    file = open('lokesh.txt','r')
    for each in file:
        print(each)


def write():
    file = open('lokesh.txt','w')
    file.write("This is the command          ")
    file.write("It allows us to write in a particular file")
    file.close()


def append():
    file = open('lokesh.txt','a')
    file.write("Today tommorow \n")
    file.close()

print("Enter the option:\n1.read the file \n2.Write the file \n3.append the file")
i=1
while i==1:
    option = input("Enter the option:  ")
    if option == '1':
        read()
    elif option == '2':
        write()
    elif option == '3':
        append()
    elif option == '4':
        exit()
    else:
        print("invalid option")
