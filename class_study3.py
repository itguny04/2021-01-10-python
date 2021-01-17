class car:
    def __init__(self, model, brand):               # 생성자
        self.model = model
        self.brand = brand
        self.speed = 0
    
    def speed_up(self):                             # 속도 증가
        self.speed += 10
        print("현재 속도: {}km/h".format(self.speed))

    def speed_down(self):                           # 속도 감소
        self.speed -= 10
        print("현재 속도: {}km/h".format(self.speed))
        if self.speed == 0:
            print("꺼짐")

    def print_name(self):
        print('브랜드: {} \n모델: {}'.format(self.brand, self.model))

class suv(car):
    def __init__(self, model, brand):               # 생성자(suv)
        car.__init__(self, model, brand)
    
class sedan(car):       
    def __init__(self, model, brand):               # 생성자(sedan)
        car.__init__(self, model, brand)



car1 = suv('펠리세이드', '현대')
car2 = sedan('AMG GT', 'Benz')


car1.print_name()
car2.print_name()
    
        