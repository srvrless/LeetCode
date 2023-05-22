from collections import deque

arr = [1, 0, 2, 3, 0, 4, 5, 0]
dq = deque(arr)
for i, y in  (list(dq)):
    if y==0:
        dq.insert(i,0) 

    print(dq)
