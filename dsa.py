### 

import time 

start_time =time.time()

def myprogram(n):
    for i in range(1,n+1):
        print(i + 10)

myprogram(20)

print(f"total time :{time.time()-start_time}")       