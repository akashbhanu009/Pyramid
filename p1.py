#from sys import argv
#print(argv[1]+argv[2])
#print(int(argv[1])+int(argv[2]))

#from sys import argv
#print("length of argument",len(argv))
#for x in argv:
#    print(argv[1] if (argv[1]>argv[2] and argv[1]>argv[3]) else argv[2] if(argv[2]>argv[1] and argv[2]>argv[3]) else argv[3],"Big Number")

n="Learning Python"
print(len(n))
i=0
for a in n:
    print(n[:i-len(n):])
    i+=1