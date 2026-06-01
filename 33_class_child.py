# # 상속
# # --> 부모(슈퍼) 클래스의 코드를 자식(서브) 클래스가 물려받는 것

# class Animal: # 클래스 정의 - 부모(슈퍼) 클래스
#     def __init__(self): # 생성자
#         self.height = 30 # 인스턴스 변수
    
#     def get_height(self): # 인스턴스 메서드
#         print(f'Animal {self.height}')

# fubao = Animal() # 인스턴스(객체) 생성
# fubao.get_height() # 인스턴스 메서드 호출

# class Dog(Animal): # 자식(서브) 클래스 정의 class 자식클래스명(부모클래스명):
#     pass

# class Cat(Animal): # 자식(서브) 클래스 정의
#     pass

# mung = Dog()
# mung.get_height() # 상속받은 인스턴스 메서드 호출

# yaong = Cat()
# yaong.get_height()

# print(fubao)
# print(mung)
# print(Cat)

# -----------------------------------------------------
# class Animal: # 클래스 정의 - 부모(슈퍼) 클래스
#     def __init__(self): # 생성자
#         self.height = 30 # 인스턴스 변수
    
#     def get_height(self): # 인스턴스 메서드
#         print(f'Animal {self.height}')

# class Dog(Animal):
#     def cry(self):
#         print('멍멍')
    
# class Cat(Animal):
#     def run(self):
#         print('살금살금')

# fubao = Animal()
# mung = Dog()
# yaong = Cat()

# fubao.get_height()
# print('-'*50)
# mung.cry()
# print('-'*50)

# yaong.get_height()
# yaong.run()

# -------------------------------------------
# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def hello(self):
#         print(f'안녕하세요 저는 {self.name}입니다')

# class Child(Parent):
#     pass

# person1 = Parent('김슈퍼')
# person1.hello()

# person2 = Child('김서브')
# person2.hello()

# print(person1)
# print(person2)

# ------------------------------------------------
# class Parent:
#     def __init__(self, name):
#          self.name = name
    
#     def hello(self):
#         print(f'안녕하세요 저는 {self.name}입니다')

# class Child(Parent):
#     def bye(self):
#         print(f'{self.name}은(는) 떠납니다')

# person1 = Parent('김슈퍼')
# person2 = Child('김서브')

# person1.hello()
# print('-'*50)
# person2.bye()

# ----------------------------------------------
# class Parent:
#     def __init__(self, name):
#          self.name = name
    
#     def hello(self):
#         print(f'안녕하세요 저는 {self.name}입니다')

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def bye(self):
#         print(f'{self.age}살인 {self.name}은(는) 떠납니다')

# person1 = Parent('김슈퍼')
# person2 = Child('김서브', 20)

# person1.hello()
# person2.hello()
# person2.bye()

# ----------------------------------------------
# class Parent:
#     def __init__(self, name):
#          self.name = name
    
#     def hello(self):
#         print(f'안녕하세요 저는 {self.name}입니다')

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def bye(self):
#         super().hello() # 부모의 인스턴스 메서드를 호출
#         print(f'{self.age}살인 {self.name}은(는) 떠납니다')

# person1 = Parent('김슈퍼')
# person2 = Child('김서브', 20)

# person1.hello()
# person2.bye()
 # -------------------------------------
class Car: # 부모(슈퍼) 클래스
    max_oil = 50 # 클래스 변수 --> 최대 주유량

    def __init__(self, oil):
        self.oil = oil # 인스턴스 변수 --> 현재 기름량

    def add_oil(self, oil):
        if oil <= 0: # 0이하의 주유는 진행하지 않는다.
            return # 함수 종료
        self.oil += oil # oil만큼 기름 넣는다.
        if self.oil > self.max_oil: # 최대 주유량보다 크다면(넘치면)
            self.oil = Car.max_oil # 현재 주유량을 최대 주유량으로 설정
    
    def car_info(self):
        print(f'현재 주유 상태(기름량) : {self.oil}')

car1 = Car(20)
car1.car_info()
car1.add_oil(40)
car1.car_info()
        
