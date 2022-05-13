l2 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
ls = []

def f(l):
    if l != []:
        if type(l[0]) != list:          
            ls.append(l.pop(0))
        else:
            f(l[0])   

def sil(l1):
    if l1 == []:
        return 1
    if type(l1[0]) != list:
        return 1  
    if l1[0] == []:     
        l1.pop(0)
    else:
        sil(l1[0])

while True:
    if l2 != []: 
        if l2[0] == []:
            l2.pop(0)
        f(l2)
    else:
        break   
    if type(l2) == list: 
        sil(l2)
   
print(ls)
