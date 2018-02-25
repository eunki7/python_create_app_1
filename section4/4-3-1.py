#리스트 자료형(순서O, 중복O, 수정O, 삭제O)

#선언
a = []
b = list()
c = [0, 0, 1, 2]
d = [0, 1, 'car', 'apple', 'apart']
e = [0, 1, ['car', 'apple', 'apart']]

#인덱싱
print('#=====#')
print('d - ',type(d),d)
print('d - ',d[1])
print('d - ',d[0]+d[1]+d[1])
print('d - ',d[-1])
print('e - ',e[-1][1])
print('e - ',e[-1][1][4])
print('e - ',list(e[-1][1]))

#슬라이싱
print('#=====#')
print('d - ',d[0:3])
print('d - ',d[2:])
print('e - ',e[2][1:3])

#리스트 연산
print('#=====#')
print('c + d - ',c + d)
print('c * 3 - ',c * 3)
#print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ",'hi' + str(c[0]))


#리스트 수정, 삭제
print('#=====#')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print('c - ', c)

#리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(5))
a.insert(2,7)
print('a - ', a)
a.reverse()
a.remove(1)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))
ex = [8, 9]
a.extend(ex)
print('a - ', a)

#삭제 remove, pop, del

#반복문 활용
while a:
    l = a.pop()
    print(2 is l)
