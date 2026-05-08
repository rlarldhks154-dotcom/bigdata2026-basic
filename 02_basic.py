# 연산자
# 산술 연산자
# + - * /(나누기, 무조건 실수형태로) %(나머지) //(몫) **(거듭제곱)

# 70쪽 동전교환기
# 10000원짜리 지폐를 500원, 100원짜리 동전으로 교환
money = 10000
print(money // 500)
print(money // 100)

print()
# 몫, 나머지 --> 구입 가능한 사탕의 수
print(money)
price = 450
numCandy = money // price
change = money % price
print(numCandy)
print(change)

print()

# 대입 연산자 =
# 복합 대입 연산자 += -= *= /= //= %=
a = 10
a += 10 # a = a + 10
print(a) # 20

a -= 5 # a = a -5
print(a)

a *= 2 # a = a * 2
print(a)

print()

# 비교 연산자
# > < >=(이상) <=(이하) ==(같다) !=(같지 않다)
print(10 == 10) # True
print(10 > 20) # False
print(10 != 20) # True

print()

# 논리 연산자
# and or not
a = 10
b = 60
print(a < 50 and b > 50) # True
print(a < 50 or b < 50) # True
c = a < 50
print(not c)

print()

# 문자열 연산자
# + 연결(이어준다)
# * 반복
print('=' * 50)
head = '파이썬'
tail = '짱!'
print(head + tail)
print('=' * 50)

print()

# in 연산자
print(head in '파이썬 짱 좋아!!!') #True
print(tail in '파이썬 짱 좋아!!!') #False
print(head not in '파이썬 짱 좋아!!!') #False