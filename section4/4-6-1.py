import pandas as pd
#xlrd, openpyxl

#기본 읽기1
#df = pd.read_excel('c:/section4/excel_s1.xlsx')
#df = pd.read_excel('c:/section4/excel_s1.xlsx',sheet_name=0)
#print(df)
#print(df.head())
#print(df.tail())

#행, 푸터 스킵
#df = pd.read_excel('c:/section4/excel_s1.xlsx', skiprows=[0], skip_footer=45)
#print(df)

#헤더 정의(1)
#df = pd.read_excel('c:/section4/excel_s1.xlsx', header=0)
#print(df)
#print(list(df))
#print(list(df.columns.values))

#헤더 정의(2)
#df = pd.read_excel('c:/section4/excel_s1.xlsx', skiprows=[0],header=None, names=["state",2003,2004,2005])
#print(df)
#print(list(df))
#print(list(df.columns.values))

#특정 값 치환
#df = pd.read_excel('c:/section4/excel_s1.xlsx', header=0, na_values='...', converters={"2003": lambda w: w if w > 60000 else None})
#print(pd.isnull(df))
#print(df)

#실습 정리 및 인덱스 재 정의
# df = pd.read_excel('c:/section4/excel_s1.xlsx', header=0)
# print(df)
# print(df.rename(index=lambda x : x+1))
# print(list(df.rename(index=lambda x : x+1).index))
