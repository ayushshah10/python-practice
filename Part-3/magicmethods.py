class result:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2

    # def __repr__(self):
    #     return 'my name is {}'.format(self.name)
    
    def __mul__(self,other):
        return (self.val1 * other.val1 ) * (self.val2 * other.val2)

r1 = result(23,11)
r2 = result(23,10)
print(r1*r2)