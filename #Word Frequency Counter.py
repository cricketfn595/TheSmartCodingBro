#Word Frequency Counter
def word_count(sentence):
    wordlist=[]
    word=[]
    count=1
    for i in sentence:
        if i != " ":
            word.append(i)
        else:
            wordlist.append(word)

    wordcount=[]
    for i in wordlist:
        if i in wordlist:
            wordcount.append(count+1)
            count+=1
        else:
            wordcount.append(count)

    return wordcount

Sentence=input("Enter a sentence: ")
print(word_count(Sentence))




