def exp_recur(x, k):
    #ver se nao tem q ser em IEEE
    if k < 0:
        return 1 / exp_recur(x, (k * -1))
    elif k == 0:
        return 1
    elif k % 2 == 0:
        return (exp_recur(x, (k / 2)) ** 2)
    else:
        return exp_recur(x, k-1) * x
    
raizquad_2 = 1.4142135623730950488

def raiz(x):
    pass

def bailey():
    pass

def lut():
    pass