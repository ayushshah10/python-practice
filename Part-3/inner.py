class Outer:
    def __init__(self,name):
        self.name = name
        # self.lap = self.Inner() to initialise instance of object of inner class another way

    def show(self):
        print(self.name)

    class Inner:
        def __init__(self,roll):
            self.roll = roll

        def show(self):
            print(self.roll)


a = Outer('apshah')
a.show()

lap = Outer.Inner('4')
lap.show()