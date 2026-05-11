# while
# <형식>
# while 조건식:
#   참이면 이 코드를 수행 # <-- 조건이 거짓이 될 때까지 반복

# 무한 반복
# while True: # 터미널에서 ctrl + c 누르면 강제종료(윈도우, 맥 동일) 
#     print('ㅋ', end = '')

# year = 1
# while year <= 3:
#     print(f'서당개 {year} 년')
#     year += 1
# print('풍월을 읊습니다.')

# 112p
# result = None #None : 없다! (예약어)
# while result != 'y':
#     print('파이썬 좋아!')
#     result = input('계속하려면 입력:(종료:y)')

# print('종료') # while 다 끝나고 난 뒤에 실행

# -----------------------------------------------

# 캐릭터 기본 체력이 100
# 정수 데미지 입힌다 - input()
# 체력이 0이 되면 종료
# hp = 100 # 체력
# while hp > 0: # 체력이 0보다 크다면 계속 반복
#     print(f'주인공의 체력은 {hp}입니다!')
#     damage = int(input('얼마의 데미지를 입힐까요?'))
#     # 체력 - 데미지 --> 남은 체력
#     hp -= damage # hp = hp - damage

# print('주인공의 체력이 0이 되었으므로 게임을 종료합니다!')

#--------------------------------------------------
# 114p
# while True:
#     num = int(input('번호 입력(종료:0):'))
#     if num == 0:
#         break
#     print('while 무한루프 반복중')

# --------------------------------------------
# continue --> 이번 차례는 건너뛰고 계속 진행
# 114p
for x in range(1,31):
    if x % 7 != 0:
        continue
    print(f'7의 배수: {x}')