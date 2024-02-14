def writef(fn):
    color = ['red','blue','green']
    with open(fn,'w') as abc:
        for c in color:
            abc.write("%s\n" % c)


writef('Part-3/abc.txt')

cont = open('Part-3/abc.txt')
print(cont.read())