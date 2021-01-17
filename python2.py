class Test1:
    def __init__(self):
        self.num = 500
    def this(self):
        return self.num

a = Test1()
b = a.this()
print(b)

class Test2:
    def __init__(self):
        pass
    def __add__(self, position):
        return str(position) + 'hello'

print(Test2()+10) # return = 'hello'

