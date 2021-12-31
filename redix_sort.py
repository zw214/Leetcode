def redix_sort(li):
    max_num = max(li)
    it = 0
    while 10**it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # buckets done
        li.clear()
        for buc in buckets:
            li.extend(buc)

        it += 1

import random
li = list(range(1000))
random.shuffle(li)
print(li)
redix_sort(li)
print(li)