# 113p

# 구구단 2단
# for i in range(1,10):
#     print(f'2 x {i} = {2 * i}') # 2 x 1 = 2

# # 단을 입력받아 구구단 출력
# num = int(input('단 입력 : '))
# for i in range(1,10):
#     print(f'{num} x {i} = {num * i}')

# 구구단 전체
# 단 --> 2단 ~ 9단 --> dan 변수 이름
# 곱해지는 수 --> 1 ~ 9 --> i 변수 이름
# for dan in range(2, 10):
#     print(f'----{dan}단----') # 단 제목
#     for i in range(1, 10):
#         print(f'{dan} x {i} = {dan * i}')

# 중첩 for이용 - 김밥 배합 출력
main = ['베이컨', '크래미']
side = ['당근', '오이']
x = 1
for m in main:
    for s in side:
        print(f'{x} : {m} + {s} + 계란')
        x += 1