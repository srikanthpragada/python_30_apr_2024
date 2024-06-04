from threading import *
import threading 
import time 


class PrintThread(Thread):
    def run(self):
        time.sleep(5)
        for i in range(1, 11):
            print(f"Child {i}", end=' ')


print("Main Thread!!!")

p = PrintThread() 
p.start() 

print(f"No. of threads : {threading.active_count()}")

for i in range(1, 11):
    print(f"Main {i}", end=' ')



print("\nThe End")

