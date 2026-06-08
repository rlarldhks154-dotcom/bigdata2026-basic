# 0번 열 - 도선관 코드, 1번 열 - 도서관명, 2번 열 - 주소, 3번 열 - 상세 주소
# 4번 열 - 전화번호, 5번 열 - 팩스번호, 6번 열 - 홈페이지, 7번 열 - 개관 시간
# 8번 열 - 휴관일

# csv 라이브러리 불러오기
from csv import * # csv 라이브러리 안 모든 함수를 가져와라. 호출 시 함수명으로 호출 가능

file = open('library.csv','r')
read_file = reader(file) # csv안의 reader함수를 불러온다 -> file 객체 내용 다 읽기

library_list = []
for line in read_file:
    library_list.append(line)
file.close()

while True:
    search_word = input('\n검색어 입력 (종료:0) : ')
    if search_word == '0':
        print('\n[도서관 정보 검색 시스템 종료]')
        break
    print('\n[도서관 정보 검색 결과]')
    for line in library_list:
        if search_word in line[1]: # 찾는 단어가 line[1](도서관명)에 포함되어 있니?
            print(f'{line[1]} / {line[2]} / {line[4]}') # 도서관명, 주소, 전화번호
