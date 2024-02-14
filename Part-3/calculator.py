class Calc:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2  = n2

    def add(self):
        n3 = self.n1 + self.n2
        return n3
    
    def sub(self):
        n3 = self.n1 - self.n2
        return n3
    
    def mul(self):
        n3 = self.n1 * self.n2
        return n3
    
    def div(self):
        n3 = float(self.n1 / self.n2)
        return n3
    


print('Enter 1 to add two numbers')
print('Enter 2 to sub two numbers')

print('Enter 3 to multiply two numbers')
print('Enter 4 to divide two numbers')
n = int(input('Enter your choice'))

n1 = int(input())
n2 = int(input())

c = Calc(n1,n2)
if n==1:
    print(c.add())
if n==2:
    print(c.sub())
if n==3:
    print(c.mul())
if n==4:
    print(c.div())    