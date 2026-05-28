name = {'최재원' : '010-1111-1234', '최지윤': '010-2222-1234', '김연수': '010-3333-1234', '김연우': '010-4444-1234', '김가현': '010-5555-1234', '김혜현': '010-6666-1234'}
print(name)
print(list(name))
search_name = input('찾는 친구 이름을 입력하세요 : ')
if search_name in name:
    print(f"{search_name}의 연락처는 {name[search_name]}입니다.")
else:
    print(f"{search_name}라는 이름의 친구는 연락처에 없습니다.")