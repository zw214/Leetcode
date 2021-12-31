maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [
    lambda x,y: (x+1, y),
    lambda x,y: (x-1, y),
    lambda x,y: (x, y-1),
    lambda x,y: (x, y+1)
]

def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while len(stack)>0:
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stack:
                print(p)
            return True
        #x-1, y; x+1, y; x, y+1; x, y-1
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2 # 2 passed already
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()

    else:
        print('no road')
        return False

maze_path(1,1,8,8)
