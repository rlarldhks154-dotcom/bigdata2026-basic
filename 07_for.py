# for와 문자열
hello = '안녕하세요!'
for h in hello:
    print(h)

print('-' * 50)

# for와 리스트
li = ['푸바오', 100, 3.141592, '아이바오', '러바오']
for i in li:
    print(i)

print('-' * 50)

# for와 딕셔너리
menu = {'김밥':3000, '라면':5000, '떡볶이':4000}
for m in menu:
    print(m) # key가 출력

for m in menu:
    print(menu[m]) # key(m)에 해당하는 값이 출력

for k, v in menu.items():
    print(f'key:{k}, value:{v}')

print('-' * 50)

for i in range(100):
    print(i) # 0~99

print('-' * 50)

for i in range(1, 31):
    print(i, end=' ')

print('-' * 50)

for i in range(1, 31, 2): # 홀수만
    print(i, end=' ')

print('-' * 50)

for i in range(30, 0, -1): # 역순
    print(i, end= ' ')