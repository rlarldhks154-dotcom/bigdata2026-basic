# 람다 표현식
# --> 익명 함수 (함수 이름이 없다!)
# <형식>
# lambda 매개변수들: 식

# 1) def
def plus_five(x):
    return x + 5

result = plus_five(10)
print(result)
print('-' * 50)

# 2) lambda
result_plus_five = lambda x: x + 5
print(result_plus_five(10))

print('-' * 50)

# 람다 표현식을 인수로 사용
# lambda x: x + 10
# map(함수, 시퀀스 자료형)
result = map(lambda x: x + 10, [30, 20, 10])
print(result)
print(list(result)) # list로 형변환

# filter(람다 함수, 시퀀스 자료형)
# --> 참(True)인 것만 나온다!
result2 = filter(lambda x: x < 20, [30, 20, 10]) # 참(True)
print(list(result2))