class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print('{0}이(가) 공부해서 {1} 성적을 받았습니다.'.format(self.name, self.grade))

s1 = Student("Choi ho yun", 'A+')
s1.study()