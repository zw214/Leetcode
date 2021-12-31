import heapq
import random

li = list(range(100))
random.shuffle(li)

print(li)

heapq.heapify(li) # create heap
print(li)

n = len(li)
for i in range(n):
    print(heapq.heappop(li), end=',') # 