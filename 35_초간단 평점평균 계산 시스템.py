# 학점 환산 기준 (A=4.5, B=3.5, C=2.5, F=0.0)
grade_map = {'A': 4.5, 'B': 3.5, 'C': 2.5, 'F': 0.0}

def subject():
    """수강 강좌정보 입력 함수"""
    while True:
        title = input('과목명(0은 종료) : ')
        if title == '0':
            break
        credit = int(input('학점 수 : '))
        grade = input('취득학점(A,B,C,F) : ')
        course.append([title, credit, grade])

course = []
while True:
    choice = int(input('1.수강 강좌정보 입력 2.평균평점 확인 0.종료 : '))
    
    if choice < 0 or choice > 2:
        print('없는 번호!\n')
        continue
        
    elif choice == 1:
        print('\n< 수강 강좌정보 입력 >')
        subject()
        print('< 수강 강좌정보 입력 종료 >\n')
        
    elif choice == 2:
        print('\n< 수강 강좌 목록 >')
        print('과목명\t학점수\t학점')
        print('-' * 20)
        
        total_credit = 0  # 총 학점 수
        total_score = 0   # (학점 * 평점) 총합
        
        for item in course:
            title, credit, grade = item
            print(f"{title}\t{credit}\t{grade}")
            
            score = grade_map.get(grade, 0.0)
            total_score += credit * score
            total_credit += credit
            
        print()
        
        # 평균평점 계산 및 출력 (소수점 둘째 자리까지)
        if total_credit > 0:
            gpa = total_score / total_credit
            print(f"평균평점: {gpa:.2f}\n")
        else:
            print("등록된 강좌가 없습니다.\n")
            
    elif choice == 0:
        print('초간단 평점평균 계산 시스템 종료!')
        break # 무한 루프 종료