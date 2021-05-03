def incSequence(Lis):
    Len = len(Lis)
    LenUnique = len(set(Lis))
    print(Len,LenUnique)
    DiffLen= Len-LenUnique
    print(DiffLen)

    if(Len%2==0):
        print("First")
    else:
       if(Len%2==0):
            print("Second")
        else:
            print("First") 
""""


    
    if(Len!=LenUnique):
        print("Entered if 1")
        if(DiffLen%2==0):
            print("First")
        else:
            print("Second")
    elif(Lis==(Lis.sort())):
        print("Entered Elif")
        print("First")
    else:
        print("Entered Else 3")
        if(Len%2==0):
            print("Second")
        else:
            print("First")
 """       
T = int(input())
for i in range(T):
    N = int(input())
    Lis = list(map(int,input().split()))
    incSequence(Lis)
    
