def add(dic,freq,word):
    if freq in dic:
        dic[freq].append(word)
    else:
        dic[freq]=list(str(word))
    return None


def rem(words,word,freq):
    for x in range(0,freq):
        words.remove(word)


def freqWords(words):
    freq=0
    dic={}
    leng=len(words)
    words=words.sort()
    for x in range(0,leng,1):
        for y in range(x+1, leng):
            if words[x]==words[y]:
                freq=freq+1
        add(dic,freq+1,words[x])
        x=x+freq
        freq=0
        #rem(words,words[x],freq)
    return dic


print(freqWords(['no','sentence','can','begin','with','because','because','because','it', 'is', 'a']))