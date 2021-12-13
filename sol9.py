#!/usr/bin/python3
import sys
from collections import deque
from functions import get_data

if __name__=='__main__':
    # get_data(9,2021)
    infile = sys.argv[1] if len(sys.argv)>1 else 'inp9'
    caveMap = [[int(height) for height in line.replace('\n','')] for line in open(infile)]
    moveArr = [[-1,0], [1,0], [0,1], [0,-1]]
    ans1 = 0
    for i in range(len(caveMap)):
        for j in range(len(caveMap[0])):
            flag = True
            for k in range(len(moveArr)):
                x = i + moveArr[k][0]
                y = j + moveArr[k][1]
                if(0<=x<len(caveMap) and 0<=y<len(caveMap[0]) and caveMap[x][y]<=caveMap[i][j]):
                    flag =False
            if(flag):
                ans1 += caveMap[i][j] + 1
    print(ans1)

    sizeArr = []
    done = set()
    for i in range(len(caveMap)):
        for j in range(len(caveMap[0])):
            if((i,j) not in done and caveMap[i][j]!=9):
                size = 0
                que = deque()
                que.append((i,j))
                while(que):
                    (i,j) = que.popleft()
                    if((i,j) in done):
                       continue
                    done.add((i,j))
                    size += 1
                    for k in range(len(moveArr)):
                       x = i + moveArr[k][0]
                       y = j + moveArr[k][1]
                       if(0<=x<len(caveMap) and 0<=y<len(caveMap[0]) and caveMap[x][y]!=9):
                            que.append((x,y))
                sizeArr.append(size)
    sizeArr.sort(reverse=True)
    print(sizeArr[0]*sizeArr[1]*sizeArr[2])
