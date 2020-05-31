tuple_x = (6, 4)
tuple_x[0] = 4
tuple_x[1] = 1
print(tuple_x)

#이렇게 정해져있으면 에러가 남

tuple_x = (6, 4)
tuple_x = (4, 1)
tuple_x = (4, 1, 7)

print(tuple_x)
#미리 생성되지 않은 객체의 경우 실행됨 위에꺼 삭제하고

list_x = []  #list를 선언, [4, 1, 7]이 실행됨 파이썬에서 제공하는 list는 가변타입이기 떄문
list_x.append(4)
list_x.append(1)
list_x.append(7)

