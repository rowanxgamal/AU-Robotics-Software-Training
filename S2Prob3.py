#string=str(input("Enter a string: "))
str1="abcd"
str2="cdba"

if len(str1)!=len(str2):
    print("Not anagrams")
else:
    count1={}
    for ch in str1:
        count1[ch]=count1.get(ch,0)+1
    count2={}
    for ch in str2:
        count2[ch]=count2.get(ch,0)+1
    if count1==count2:
        print("Anagrams")
    else:
        print("Not anagrams")