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
        if(i!=' ' and i!='.' and i!='?' and i!='!'):
            letters+=1
    return letters

speech=input("Enter a sentence: ")
sentences=countSentences(speech)
words=countWords(speech)
letters=countLetters(speech)

#Formula: 5.89 x (characters/words) – 0.3 x (sentences/words) – 15.8
print("Output: ",int(5.89*(letters/words)-0.3*(sentences/words)-15.8+0.5))