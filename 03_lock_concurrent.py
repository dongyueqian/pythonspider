import threading
import time

class Account:
    def __init__(self, balance):
        self.balance = balance

def draw(account, amount):
    if account.balance >= amount:
        time.sleep(0.1) # 会引发阻塞，进而切换线程
        print(threading.current_thread().name, "取钱成功----1")
        account.balance -= amount
        print(threading.current_thread().name, "余额----2", account.balance)

    else:
        print(threading.current_thread().name, "取钱失败,余额不足----3")

if __name__ == '__main__':
    account = Account(10000)
    cu1 = threading.Thread(target=draw, args=(account, 8000), name="cu1")
    cu2 = threading.Thread(target=draw, args=(account, 8000), name="cu2")
    cu1.start()
    cu2.start()