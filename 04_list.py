# 빈 리스트 생성
li = []
print(li)

li2 = list()
print(li2)

# append() --> 맨 뒤에 값(하나) 추가
li.append('푸바오')
print(li)

li.append(100)
print(li)

li.append(3.141592)
print(li)

li.append('루이바오')
li.append('후이바오')
print(li)

# 인덱싱 --> 0부터 시작한다. -1 맨 끝값
print(li[0])
print(li[3])
print(li[-1])

# 슬라이싱
# <형식>
# 리스트명[시작 인덱스번호:끝 인덱스번호+1 증감값]
#       증감값은 보통 생략(1씩 증가가 대부분)
print(li[1:4])
print(li[1:]) # 끝 번호 생략 가능(끝까지)
print(li[:3]) # 첫 번호 생략 가능(처음부터)
print(li[:]) # 모두(전체)
print(li[::-1]) #반전

# 리스트의 값(요소) 변경
li[3] = '아이바오' # 인덱스 번호 3번 자리에 아이바오로 수정
print(li)