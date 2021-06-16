def add(dic,freq,word):
    if freq in dic:
        dic[freq].add(word)
    else:
        dic[freq]={word}
    return None


def edit(s):
    s=s.lower()
    t=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    s1=''
    for x in range(len(s)):
        if (s[x] in t) or (s[x]=="-"):
            s1=s1+s[x]
    return s1


def stol(dic):
    for x in dic.keys():
        dic[x]=list(dic[x])
    return None


def freqWords(words):
    dic={}
    leng=len(words)
    # print(words)
    words.sort()
    # print(words)
    for x in range(leng):
        words[x]=edit(words[x])
    for x in range(leng):
        c=words.count(words[x])
        add(dic,c,words[x])
    stol(dic)
    return dic


print(freqWords(['no','Sentence','can','begin','with','because','because','because','it','it', 'is', 'a']))