import pandas as pd
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#기본 읽기2
#df1 = pd.read_excel('c:/section4/excel_s1.xlsx',  header=0)

#Columns 값 수정
#df1['State'] = df1['State'].str.replace(' ', '|')
#print(df1)

#평균 컬럼 추가
#df1['Avg'] = df1[['2003','2004','2005']].mean(axis=1).round(2)
#print(df2)

#합계 컬럼 추가
#df1['Sum'] = df1[['2003','2004','2005']].sum(axis=1)
#print(df1)

#최대값 출력
#print(df1)
#print(df1[['2003','2004','2005']].max(axis=0))

#최소값 출력
#print(df1)
#print(df1[['2003','2004','2005']].min(axis=0))

#상세 분석 정보 출력
#print(df1.describe())

#엑셀 쓰기 (색상 설정은 openpyxl)
#df1.to_excel('c:/section4/result_s1.xlsx')
#df1.to_excel('c:/section4/result_s1.xlsx',index=None)

#컬럼 연산 추가
# df2 = pd.read_excel('c:/section4/excel_s2.xlsx', header=0)
# df2[['Units','UnitCost']] = df2[['Units','UnitCost']].astype(int)
# df2['Custom1'] = df2['Units'] * df2['UnitCost']
# df2['Custom2'] = df2['Total'] * 10
#
# print(df2)

#엑셀 쓰기 (색상 설정은 openpyxl)
# df2.to_excel('c:/section4/result_s2.xlsx')
# df2.to_excel('c:/section4/result_s2.xlsx',index=None)
