from collections import deque


adjacency_list=[[1,2],
                [0,2,3,4],
                [0,1,3,6,7],
                [1,2,5,6],
                [1,5,8],
                [3,4,8],
                [2,3,8,9],
                [2,9],
                [4,5,6,9],
                [6,7,8]]

#t=int(input())
#T=int(input())
#node=int(input())
#test case: t=2,T=17 or 20 and node=0 --> num=3
#test case: t=2,T=17 node=4 --> num=3
#test case: t=2,T=20 node=4 --> num=4
t=2
T=17
node=0 
visited=[False]*len(adjacency_list)
distance=[float('inf')] * len(adjacency_list)
flags=[]

distance[node]=0
def bfs(node):
    queue=deque()
    queue.append(node)
    visited[node]=True
    covered=0
    num=0
    while(queue):
        currentnode=queue.popleft()
        for i in adjacency_list[currentnode]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
                if distance[currentnode]+t <distance[i]:
                    distance[i]=distance[currentnode]+t
        if (distance[currentnode]+covered)*2<=T :
            covered+=distance[currentnode]
            #print(covered*2,"at node",currentnode)
            if currentnode!=node:
                num+=1
                flags.append(currentnode)
        else:
            return num,covered*2

num,covered=bfs(node)
print(distance)
print("Number of flags: {x}, flags are {y}".format(x=num,y=flags))
print("Actual distance covered: {x}".format(x=covered))

#unique time per edge: use dijkstra             