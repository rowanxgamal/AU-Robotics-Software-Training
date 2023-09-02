# Description: Print a half pyramid of a specified height

x=int(input())
while x<1 or x>8:
    x=int(input("Add another input between 0 and 8 :"))

#clean code
for i in range(1,x+1):
    print(" "*(x-i)+"#"*i+"  "+"#"*i)


