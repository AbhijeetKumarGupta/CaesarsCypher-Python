import sys 

#variable to hold out arguments  
arg1 = str(sys.argv[1])
arg2 = str(sys.argv[2])
arg3 = str(sys.argv[3])
arg4 = str(sys.argv[4])
arg5 = str(sys.argv[5])
arg6 = str(sys.argv[6])
arg7 = str(sys.argv[7])
arg8 = str(sys.argv[8])

#just for testing purpous, you can remove it if you want
print(arg1)
print(arg2)
print(arg3)
print(arg4)
print(arg5)
print(arg6)
print(arg7)
print(arg8)

#element we will need later
#you can use either lower or upper i have made it to work with lower
#but if you want you can just rename lower to upper everywhere inside loop, rest of the code will be same
space = ' '
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# encryption part
if(arg8 == "enc"):
    key = int(arg6)
    file1 = open(arg4, "a")  # append mode 
    with open(arg2, 'r') as r:
        for line in r:
            for i in range(0,len(line)):
                if(line[i] != space):
                    for j in range(0,26):
                        if(line[i] == lower[j]):
                            if((j+int(key))>25):
                                file1.write(lower[((j+int(key))%25)-1])
                            else:
                                file1.write(lower[j+int(key)])
                elif(line[i] == space):
                    file1.write(space)
            print()

    file1.close()

# decryption part
elif(arg8 == "dec"):
    key = int(arg6)
    file1 = open(arg4, "a")  # append mode 
    with open(arg2, 'r') as r:
        for line in r:
            for i in range(0,len(line)):
                if(line[i] != space):
                    for j in range(0,26):
                        if(line[i] == lower[j]):
                            if((j-int(key))<0):
                                file1.write(lower[(26+(j-int(key)))])
                            else:
                                file1.write(lower[j-int(key)])
                elif(line[i] == space):
                    file1.write(space)
            print()

    file1.close()
elif(arg8 == "" or arg6 == "" or arg4 == "" or arg2 == ""):
    print("ERROR!")
