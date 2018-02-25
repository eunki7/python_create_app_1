#딕셔너리 자료형(순서X, 중복X, 수정O, 삭제O)

#선언
a = { 'name': 'kim', 'phone': '01077777777', 'birth': '700124' }
b = { 0: 'Hello World!' }
c = { 'arr': [0,1,2,3] }
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)

#출력
print('a - ', a['name'])     #존재X -> 에러 발생
print('a - ', a.get('name')) #존재X -> None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))

#딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

#dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))

print('a - ', 'name' in a)
print('a - ', 'addr' in a)
