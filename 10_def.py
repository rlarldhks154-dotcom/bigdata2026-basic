# 사용자 정의 함수

# 함수 정의
# 함수 이름 --> add, 매개변수(파라미터) --> number1, number2
# def add(number1, number2):
#     print('계산 시작...')
#     return number1 + number2

# # 결과변수 = 함수이름(인수1, 인수2) # 함수 호출
# result = add(50, 60)
# print(result)

#---------------------------------------------
# 매개변수는 있고, return(반환값)이 없는 함수
# def add(num1, num2): # 함수 정의
#     print(num1 + num2)
#     print('ㅋㅋㅋㅋ')

# # 함수 호출
# add(10, 20)

#---------------------------------------------
# 매개변수는 없고, return(반환값)만 있는 함수
# def coffee(): # 함수 정의
#     print('오늘은 석쌤이 커피를 쏩니다!')
#     result = '아메리카노'
#     return result

# cup = coffee() # 함수 호출
# print(cup)

#-------------------------------------------------
# 매개변수도 없고, return(반환값)도 없는 함수
# def coffee(): # 함수 정의
#     print('커피가 나왔을까요???')
#     print('잠시 후...')
#     print('아니지롱!!! ㅋㅋㅋㅋ')

# coffee() # 함수 호출

# coffee() # 함수 또 호출

#------------------------------------------
# return(반환값)이 2개 이상인 함수
# def add_sum(n1, n2): #함수 정의
#     return n1 + n2, n1 - n2

# x, y = add_sum(1, 2) # 함수 호출
# print(x, y)

# print(add_sum(200, 100)) # 함수 호출

#-----------------------------------------
# 가변 매개변수 *args
# 함수 정의 --> 정수를 몇 개를 더해야 할지 정해지지 않았다
#               --> 가변매개변수로
# def adder(*args): # 튜플로 묶겠다(튜플 패킹) --> *
#     total = sum(args) # sum() : 합계를 구하는 내장함수
#     return total

# # 함수 호출
# result1 = adder(1, 2)
# result2 = adder(1, 3, 5, 7, 9)
# result3 = adder(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(f'result1 : {result1}')
# print(f'result2 : {result2}')
# print(f'result3 : {result3}')

#-------------------------------------------------
# 돌발퀴즈!
# 함수 정의 --> 함수 이름, 매개변수(원하는 값), return이 있다
# 함수 호출 --> 결과변수에 return값을 담는다
# 1부터 원하는 값까지 더해주는 함수(for쓰자!)
def num_total(num):
    total = 0
    for i in range(1, num+1):
        total += i # total = total + i
    return total

result = num_total(10)
print(result)