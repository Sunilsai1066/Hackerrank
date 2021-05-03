def superReducedString(s):
    Stack = []
    for i in s:
        if(Stack and i==Stack[-1]):
            Stack.pop()
        else:
            Stack.append(i)
    Str = "".join(Stack)
    if Str:
        return Str
    else:
        return "Empty String"
