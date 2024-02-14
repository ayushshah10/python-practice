def search(dict1,height,weight):
    l = {k:s for k,s in dict1.items() if s[0]>height and s[1]>weight}
    return l

dict1 = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

an = search(dict1,5.8,65)
print(an)