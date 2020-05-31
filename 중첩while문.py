#{} * {} = {} 계산 형태, format은 형식을 짖어해줌
#아래는 1단 구구단
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print("{} * {} = {}".format(i, j, i * j))
        j += 1
    i += 1


#아래는 200단까지 실행한 구구단
w = 11
while w <= 200:
    e = 1
    while e <= 200:
        print("{} * {} = {}".format(w, e, w * e))
        e +=1
    w +=1


# 300까지 실행한 구구단
a = 1
while a <= 300:
    b = 1
    while b <= 300:
        print("{}*{} = {}".format(a, b, a * b))
        b += 1
    a +=1

# {} * {} * {} = {} 3단 구구단

x = 1
while x <= 9:
    z = 1
    while z <= 9:
        v = 1
        while v <= 9:
            print("{} * {} * {} = {}".format(x, z, v, x * z * v))
            v += 1
        z += 1
    x += 1


# {} * {} * {} = {} 3단 구구단

x = 1
while x <= 9:
    z = 1
    while z <= 9:
        v = 1
        while v <= 9:
            print("{} * {} * {} = {}".format(x, z, v, x * z * v))
            v += 1
        z += 1
    x += 1

# {} * {} * {} * {} = {} 4단 구구단 ==> 구구단은 4단까지 밖에 안되나?????
x = 1
while x <= 9:
    z = 1
    while z <= 9:
        v = 1
        while v <= 9:
            c = 1
            while c <= 9:
                continue
            print("{} * {} * {} = {}".format(x, z, v, x * z * v))
            v += 1
        z += 1
    x += 1
c += 1

