#튜플 자료형(순서O, 중복O, 수정X,삭제X)

#선언
a = ()
b = (0,)
c = (0,1,2,3)
d = (0, 1, 'car', 'apple', 'apart')
e = (0, 1, ('car', 'apple', 'apart'))

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

#튜플 연산
print('#=====#')
print('c + d - ',c + d)
print('c * 3 - ',c * 3)
#print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ",'hi' + str(c[0]))

#튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))
