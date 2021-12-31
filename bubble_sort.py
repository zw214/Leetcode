import random

def bubble_sort(li):

    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:  # <
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True

        if not exchange:
            return



li = [random.randint(0, 10000) for i in range(1000)]
print(li)
bubble_sort(li)
print(li)