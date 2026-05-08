# 빈 딕셔너리 생성
a = {}
print(a)

b = dict()
print(b)

# 딕셔너리 초기화
# <형식>
# {key1:value1, key2:value2, ....}
menu = {'김밥':3000, '라면':5000}
print(menu)

print(menu['김밥'])
print(menu['라면'])

# 새로운 쌍 추가
menu['떡볶이'] = 4000
print(menu)

# 값 수정
menu['김밥'] = 3500
print(menu)

# 쌍(키와 값) 삭제
del(menu['라면'])
print(menu)

# set(세트) 자료형 --> 순서가 없다! 중복이 안된다!
a = {30, 20, 10}
print(a)

b = set() # 빈 세트
print(b)

c = {40, 20}
print(c)

# 교집합
print(a & c)

# 합집합
print(a | c)

# 차집합
print(a - c)
print(c - a)