y=input()
x=str(y)
x = x[::-1]


formula=0
flag=False
for i in x:
    if flag==True:
        z=2* int(i)
        if z>9:
            z=z%10+z/10
        formula+=z
        flag=False
    else:
        formula+=int(i)
        flag=True

if(formula%10!=0):
    print("Output: Invalid")
elif int(x[-1])==5:
    print("Output: MasterCard")
elif int(x[-1])==4:
    print("Output: Visa")
elif int(x[-1])==3:
    print("Output: American Express")
 