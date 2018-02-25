#집합(Sets) 자료형(순서X, 중복X)

#선언
a = set()
b = set([0,1,2,3])
c = set([0,3,4,5])
d = set([0, 1, 'car', 'apple', 'apart'])

print('a - ',type(a), a)
print('b - ',type(b), b)
print('c - ',type(c), c)
print('d - ',type(d), d)

#튜플 변환
t = tuple(b)
print('t - ',type(t), t)
print('t - ', t[0], t[1:3])

#리스트 변환
l = list(c)
print('l - ',type(l), l)
print('l - ', l[0], l[1:3])


#집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('l - ',s1 & s2)
print('l - ',s1.intersection(s2))

print('l - ',s1 | s2)
print('l - ',s1.union(s2))

print('l - ',s1 - s2)
print('l - ',s1.difference(s2))

#추가 & 제거
s1 = set([0, 1, 2, 3])
s1.add(4)
print('s1 - ',s1)

s1.remove(2)
print('s1 - ',s1)
