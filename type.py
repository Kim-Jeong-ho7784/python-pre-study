#튜플(tuple)은 셀수있는 수량의 순서있는 열거이다

mutable_object = [1,2,3]
immutable_object = (1,2,3)

mutable_object[0] = 4
print(mutable_object)
#0번째 요소인 1을 4로 바꿀 수 있다. --> 이처럼 가변객체는 인스턴스을 4로 바꿀 수 있다.

immutable_object[0] = 4
print(immutable_object)
#튜플은 에러가 남. 불변타입이기 때문이다.


