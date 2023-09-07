from collections import deque

str="(()))("
flag=1
mystack=deque()
for ch in str:
    if ch=='(':
        mystack.append(ch)
    else:
        if not mystack:
            flag=0
            break
        else:
            mystack.pop()
if flag==1:
    if not mystack:
        print("Balanced")
    else:
        print("Not balanced")
else:
    print("Not balanced")