def chocolateFeast(n, c, m):
    Choc = n//c
    Rem = Choc
    Res = Choc
    while Rem>=m:
        Val= Rem//m
        Re = Rem%m
        Re += Val
        Res += Val
        Rem = Re
    return Res
