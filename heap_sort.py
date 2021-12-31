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
        if j+1 <= high and li[j+1] > li[j]:
            j = j+1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            break
    li[i] = tmp

def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        sift(li, i, n-1)
    # constructed a heap

    for i in range(n-1, -1 ,-1):
        #i: the last position in heap
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)
        

