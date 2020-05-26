import threading
import time


def sq(a):
    for i in range(9):
        print("square-------")
        time.sleep(5)


def cu(a):
    for i in range(9):
        time.sleep(1)
        print("cube-------")


a = 9

t = time.time()
t1 = threading.Thread(target=sq, args=(a,))
t2 = threading.Thread(target=cu, args=(a,))

t1.start()
t2.start()

t1.join()
t2.join()
for i in range(10):
    print("main")

print(time.time() - t)
