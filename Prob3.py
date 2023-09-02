x=int(input())

a=0
b=0  
c=0
d=0
e=0
f=0
g=0
if(x>200):
    a=x/200
    x=x%200
if(x>100):
    b=x/100
    x=x%100
if(x>50):
    c=x/50
    x=x%50
if(x>20):
    d=x/20
    x=x%20
if(x>10):
    e=x/10
    x=x%10
if(x>5):
    f=x/5
    x=x%5
if(x<5):
    g=x
    x=0

print("Output: ")
if(a!=0):
    print(int(a),"x200 L.E")
if(b!=0):
    print(int(b),"x100 L.E")    
if(c!=0):  
    print(int(c),"x50 L.E")
if(d!=0): 
    print(int(d),"x20 L.E")
if(e!=0): 
    print(int(e),"x10 L.E")
if(f!=0): 
    print(int(f),"x5 L.E")
if(g!=0): 
    print(int(g),"x1 L.E")