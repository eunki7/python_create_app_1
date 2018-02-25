import matplotlib.pyplot as plt

#fig 객체 생성
fig = plt.figure()

#서브 슬롯 생성 (2행 1열)
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

#x축 생성
x = range(0, 100)

#y축 생성1
y = [v*v for v in x]

#y축 생성2
z = [v*v*2 for v in x]

#멀티 라인(1행 1열)
ax1.plot(x, y, 'b', z, 'r') #. , --

#Bar 차트(2행 1열)
ax2.bar(x, y)

#차트 실행
plt.show()
