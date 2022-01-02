
def lcs_length(x, y):
    m = len(x)
    n = len(y)

    c = [[0]*(n+1)]*(m+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]

def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  #1: top left, 2: up, 3: left
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 3

    return c[m][n], b

def lcs_trackback(x, y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(res))

# c, b = lcs('ABCBDAB', 'BDCABA')
# for _ in b:
#     print(_)

print(lcs_trackback('ABCBDAB', 'BDCABA'))



