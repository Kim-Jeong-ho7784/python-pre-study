#from 모듈의 이름 import 불러올 변수/함수/클래스 이름
# 이때 모듈의 이름에는 .py를 뺀 이름을 넣으면 된다.

from module import sum

print(sum(3,5))

#만약에 모듈에 정의된 모든 것들을 사용하려면
#from module import sum, difference, product, square

from module import sum, difference, product, square

print(difference(5,3))

# 하지만, 모듈에서 가져오려는 것이 100개 이상이면 *를 쓰면됨.
from module import *

print(sum(3, 5))
print(difference(3, 5))
print(product(3, 5))
print(square(3))