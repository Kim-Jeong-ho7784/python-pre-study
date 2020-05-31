x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
x.setdefault('e')
print(x);

x.update(a = 100)
print(x);

y = {1: 'one', 2: 'two'}
y.update({1: 'WE', 3: 'THREE'})
print(y);
#3은 없었기 때문에 추가가된다.

#한칸 띄어서 사용하는 것도 가능함.
x.update(a=900, f=60)
print(x);

y = {1:'하나', 2:'TWO', 3:'셋', 4: 'FOUR'}
y.update(zip([1,2], ['핸드폰', '김정호']))
print(y);
#zip을 쓰면 묶음지정해서 한꺼번에 바꿔주는 기능이 있다.

#pop(키)는 딕셔너리에서 특정 키 값 쌍을 삭제한 뒤 삭제 한 값을 반환
#다음은 딕셔너리 x에서 키'a'를 삭제한 뒤 10을 반환함:
x1 = {'a' : 10, 'b' : 20, 'c' : 30, 'd' :40}
x1.pop('a')
print(x1);
#앞에 띄어쓰기 하면 오류가 난다.
#키가 없을 때는 기본값만 반환함

x2 = {'a' : 10, 'b' : 20, 'c' : 30, 'd' :40 }
x2.pop('z', 0)
print(x2);
#z가 scpoe안에 없는데 입력해야할 때는 뒤에 0을 넣어줌 ('z',0)처럼..
#x2.pop('z')만 입력 시 오류가 뜸


#pop대신에 del로 특정 키 값을 삭제 가능함.
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' :40 }
del x['a']
print(x);

#.popitem은 맨 끝에 있는 것을 지워준다.
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' :40 }
x.popitem()
('d',40)
print(x);


#clear를 쓰면 모두 지워짐.
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' :40 }
x.clear()
print(x);


#get은 딕셔너리에서 특정 키를 가져옴
x1 = {'a' : 10, 'b' : 20, 'c' : 30, 'd' :40 }
print(x1.get('a'));
print(x1.get('z',0));
print(x1.get('a', 90));



#딕셔너리는 키와 값을 가져오는 다양한 메서드 제공
#items: 키-값 쌍을 모두 가져옴
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' :40 }
print(x.items());

#keys: 키를 모두 가져옴
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' :40 }
print(x.keys());

#values: 값을 모두 가져옴
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' :40 }
print(x.values());

#딕셔너리 만들기
keys = ['a', 'b','c', 'd']
x = dict.fromkeys(keys)
print(x);

#none에 숫자 추가
y = dict.fromkeys(keys, 100)
print(y);