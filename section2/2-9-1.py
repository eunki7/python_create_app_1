import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    #__init__
    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("---------------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("---------------")

    def __del__(self):
        print("delete")

user1 = UserInfo()
user2 = UserInfo()
user1.set_info("User1","010-7777-7777")
user2.set_info("User2","010-7778-7778")
user1.print_info()
print(type(user1))
print(id(user1))
print(type(user2))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)
