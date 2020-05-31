i = 1  #(불변객체)
while i <= 3:
    print("나는 잘생겼다!");
    i += 1

i = 1
while i <= 10:
    print(i)
    i += 1

i = 1
while i <= 50:
    print(i)
    i += 1

#짝수만 50까지 출력되게 할 경우
# i가 20까지 입력 되기 때문에 i <= 20 , 20 * 2 = 40까지 나온다.
i = 1
while i <= 20:
    print(i * 2)
    i += 1


# while문을 사용하여, 100이상의 자연수 중 가장 작은 23의 배수를 출력해보세요.
i = 100

while i % 23 != 0:
    i += 1

print(i)
