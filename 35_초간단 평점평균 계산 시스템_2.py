# 학점 변환 기준 (A=4.5, B=3.5, C=2.5, F=0.0)
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
    choice = int(input('1.수강 강좌정보 입력 2.평균평점 확인 3.졸업여건 확인 0.종료 : '))
    
    if choice < 0 or choice > 3:
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
        total_credit = 0
        total_score = 0
        for item in course:
            title, credit, grade = item
            print(f"{title}\t{credit}\t{grade}")
            score = grade_map.get(grade, 0.0)
            total_score += credit * score
            total_credit += credit
        print()
        if total_credit > 0:
            gpa = total_score / total_credit
            print(f"평균평점: {gpa:.2f}\n")
        else:
            print("등록된 강좌가 없습니다.\n")
            
    elif choice == 3:
        print()
        # 1. 등록 학기 체크
        semesters = int(input('총 등록 학기수 입력 : '))
        if semesters >= 8:
            print('졸업학기 충족')
        else:
            print(f'{8 - semesters}학기 부족')
            
        # 2. 수강 학점 체크
        total_credits_input = int(input('\n수강 완료 학점수 입력 : '))
        if total_credits_input >= 120:
            print('졸업학점 충족')
        else:
            print(f'{120 - total_credits_input}학점 부족')
            
        # 3. 평균 평점 체크
        gpa_input = float(input('\n총 평균평점 입력 : '))
        if gpa_input >= 2.5:
            print('졸업 평균평점 충족\n')
        else:
            print(f'{2.5 - gpa_input:.2f} 평균평점 낮음\n')
            
    elif choice == 0:
        print('초간단 평점평균 계산 시스템 종료!')
        break