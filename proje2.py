ll = [[1, 2], [3, 4], [5, 6, 7]]

def dondur(l):
    x = 1
    for i in range(len(l)-1):
        l.insert(0, l.pop(x))
        x += 1    

def f(l):
    for i in l:
        if type(i) == list:
            f(i)
    dondur(l)

f(ll)
print(ll)
