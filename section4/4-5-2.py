import pandas as pd
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#특정 문자 구분
df2 = pd.read_csv('c:/section4/csv_s2.csv',sep=';', skiprows=[0], header=None, names=["First name", "Test1", "Test2", "Test3", "Final", "Grade"])
df2['Grade'] = df2['Grade'].str.replace('"', ' ')
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1)
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)

print(df2)

#CSV 쓰기
#df2.to_csv('c:/section4/result.csv')
df2.to_csv('c:/section4/result.csv',index=False)
