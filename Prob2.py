#functions to count certain characters
def countSentences(speech):
    sentences=0
    for i in speech:
        if(i=='.' or i=='?' or i=='!'):
            sentences+=1
    return sentences

#function to count words
def countWords(speech):
    words=0
    for i in speech:
        if(i==' '):
            words+=1
    return words+1

#function to count letters
def countLetters(speech):
    letters=0
    for i in speech:
        if(i!=' ' and i!='.' and i!='?' and i!='!' and i!=',' and i!='\''):
            letters+=1
    return letters

speech=input("Enter a sentence: ")
sentences=countSentences(speech)
words=countWords(speech)
letters=countLetters(speech)

#letters=letters/words*100
grade=0.0588*(letters/words*100)-0.296*(sentences/words*100)-15.8
grade=round(grade)
if grade<1:
    print("Output: Before Grade 1")
elif grade>=16:
    print("Output: Grade 16+")
else:
    print("Output: ",grade)
print(sentences," ",words," ",letters)