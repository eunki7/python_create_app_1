import simplejson as json

#Dict(Json)선언
data = {}
data['people'] = []
data['people'].append({
    'name': 'Kim',
    'website': 'naver.com',
    'from': 'Seoul',
})
data['people'].append({
    'name': 'Park',
    'website': 'google.com',
    'from': 'Busan'
})
data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon'
})

#data = {'people': [{'name': 'Kim', 'from': 'Seoul', 'website': 'naver.com'}, {'name': 'Park', 'from': 'Busan', 'website': 'google.com'}, {'name': 'Lee', 'from': 'Incheon', 'website': 'daum.net'}]}

#Dict(Json) -> Str
e = json.dumps(data, indent=4)
print(type(e))
print(e)

#Str -> Dict(Json)
d = json.loads(e)
print(type(d))
print(d)

#json 파일 쓰기(dumps)
with open('c:/section4/member.json','w') as outfile:
    outfile.write(e)

#json 파일 읽기(loads)
with open('c:/section4/member.json', 'r') as infile:
    r = json.loads(infile.read())
    print('=====')
    #print(type(r))
    #print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
