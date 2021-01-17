class Test1:
    def __str__(self):
        return '클래스 호출 됨 ㄹㅇㅋㅋ'

print(Test())

class Test2:
    def __repr__(self):
        return '클래스 호출 됨 ㄹㅇㅋㅋ'
    
print(Test2())