import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Warehouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

u1 = Warehouse("p1")
u2 = Warehouse("p2")

print(u1.name)
print(u2.name)
print(u1.__dict__)
print(u2.__dict__)
#인스턴스 공유 클래스 변수 사용
print(u1.stock_num)
print(u2.stock_num)
