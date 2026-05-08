# # 회원이면 '어서오세요'라는 인사말 출력
# member = input('회원이십니까(y/n)')
# if member == 'y':
#     print('반갑습니다.')
# else:
#     print('회원가입을 해주세요.')

# 회원이면 '어서오세요'라는 인사말 출력
# member = input('회원이십니까(y/n)')
# if member == 'y':
#     print('반갑습니다.')
# elif member == 'n':
#     print('회원가입하세요!')
# else:
#     print('y와 n중에 입력하세요.')

# 입장료 정가 : 2만원, 1세~6세 미만 : 무료, 6세~60세 미만: 정가, 60세 이상 : 정가의 50%
age = int(input('나이 입력 : '))
price = 20000
if age < 6:
    print('입장료는 무료')
elif age < 60:
    print(f'입장료는 {price}원')
else:
    print(f'입장료는 {price*0.5}원')