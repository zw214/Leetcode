def sift(li, low, high):
    """

    :param li: list
    :param low: heap root node
    :param high: heap last element position
    :return:
    """

    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp

def topk(li, k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    #1. construct a heap
    for i in range(k, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    #2. go thru all elements
    for i in range(k - 1, -1, -1):
        # i: the last position in heap
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    #3. chushu
    return heap



import random
li = list(range(1000))
random.shuffle(li)

print(topk(li, 10))