# dict
# --> 딕셔너리 자료형

# 딕셔너리 만들 때
d = {'a':1, 'b':2, 'c':3}
print(d)
print(type(d)) # <class 'dict'>

d2 = [('a',1), ('b',2), ('c',3)]
print(d2)
print(type(d2))

# 딕셔너리로 형 변환
d2 = dict(d2)
print(d2)
print(type(d2))

# 또 다른 딕셔너리 생성 방법
d3 = dict(a = 1, b = 2, c =3)
print(d3)
print(type(d3))

print('-' * 50)
#------------------------------------------------------------------
# zip() 함수
# --> 키는 키끼리, 값은 값끼리 묶는다. (딕셔너리)
# --> 같은 인덱스 번호끼리 묶는다. (리스트, 튜플)
d4 = dict(zip(['a','b','c'],[1,2,3]))
print(d4)
print(type(d4))

li = ['a','b','c']
tu = (1,2,3)
result_zip = zip(li,tu)
print(result_zip)
print(type(result_zip))
for i in result_zip:
    print(i)
print(list(zip(li,tu))) # 리스트로 형 변환

li_1 = [1, 2]
li_2 = ['a','b','c']
li_3 = ['가','나','다']
print(list(zip(li_1,li_2,li_3)))      

for i in zip(li_1,li_2,li_3):
    print(i)

print('-'*50)
#---------------------------------------------
# 튜플은 쪼갤 수 있다 (각각의 변수로 담는다) --> 튜플 언패킹
# 튜플을 묶는다 --> 튜플 패킹 --> def func(*args):
for z1, z2, z3 in zip(li_1,li_2,li_3):
    print(f'z1 : {z1}, z2 : {z2}, z3 : {z3}')
print('-'*50)
#---------------------------------------------
# enumerate()
# for i in enumerate(li_2):
#     print(i)

# for index, value in enumerate(li_2):
#     print(f'index : {index}, value : {value}')

# print()
# for index, value in enumerate(li_2, start=1):
#     print(f'index : {index}, value : {value}')

print('-'*50)
#---------------------------------------------
# 딕셔너리와 for
for i in d4:
    print(i)

for i in d4:
    print(d4[i]) # 값(value) 출력

print('-'*50)
#---------------------------------------------
# .keys() --> 키(key)만 추출
print(d4) # {'a' : 1, 'b' : 2, 'c' : 3}
for i in d4.keys():
    print(i)

print(d4.keys()) # dict_keys(['a', 'b', 'c'])
print(list(d4.keys())) # ['a', 'b', 'c']

print('-'*50)
#---------------------------------------------
# .values() --> 값(value)만 추출
for i in d4.values():
    print(i)

print(d4.values()) # dict_values([1, 2, 3])
print(list(d4.values())) # [1, 2, 3]

print('-'*50)
#---------------------------------------------
# .items() --> 키와 값을 같이 묶어서 보여준다.
for i in d4.items():
    print(i)

for k, v in d4.items():
    print(f'k : {k}, v : {v}')

# 튜플을 묶는다 --> 튜플 패킹 --> def func(*args):
# *args --> 가변 매개변수
def func(*args):
    total = 0
    for i in args:
        total += i
    return total

result1 = func(1,2)
result2 = func(1,2,3)
result3 = func(1,2,3,4,5)
result4 = func(10, 3, 20, 50, 3, 11, 23)

print(result1,result2,result3,result4)

print('-' * 50)
# ------------------------------------------
def func2(name, *args):
    total = 0
    for i in args:
        total += i
    print(f'{name}이(가) 더한 값은 {total}입니다.')

func2('푸바오', 1,2,3)
func2('춘식이', 10,20)