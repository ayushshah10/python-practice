class Subset:
    def subset(self,set):
        return self.subsetrec([],set)

    def subsetrec(self,current,set):
        if set:
            return self.subsetrec(current,set[1:]) + self.subsetrec(current+[set[0]],set[1:])
        
        return [current]
    

print(Subset().subset([23,10,14]))


