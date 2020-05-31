#현재 진행되고 있는 수행 부분을 중단하고 바로 조건 부분을 확인하고 싶으면 continue문을 쓰면 됩니다.
#문제 : 홀수 출력
i = 0

while i < 15:
    i = i + 1
    if i % 2 == 1:
        continue
    print(i)

i = 100

while True:
    # i가 23의 배수면 반복문을 끝냄
    if i % 23 == 0:
        break
    i = i + 1

print(i)

while True:
    # i가 25의 배수면 반복문을 끝냄
    if i % 25 == 0:
        break
    i = i + 1

