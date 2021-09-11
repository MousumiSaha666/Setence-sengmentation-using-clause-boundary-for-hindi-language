import stanza
nlp=stanza.Pipeline("hi")
txt=input("Write your sentences \n")
doc=nlp(txt)
print(doc)

#Tokeniztion and senetence segmentation
import stanza
nlp = stanza.Pipeline(lang="hi", processors='tokenize')
for i, sentence in enumerate(doc.sentences): 
    print(f'=========Sentence {i+1} tokens=============')
    print(*[f'id: {token.id}\ttext: {token.text} 'for token in sentence.tokens], sep='\n')





a=[]
stopword=['और', 'कि']
# txt = "मैं अपने भाई से मिला और उसने मुझे योजना क बारे में बताया और मैं आया, जब मैं भाया।"

x = txt.split('।') 	#separating multiple sentences
n=len(x)-1 
for i in range(n):		#accessing 1 sentence at a time
    print("Sentence ",i+1, ":",x[i])			
    s = x[i].split(",")		#segmenting sentence on the basis of punctuation ,
    #a.append(s)
    print("s", s)
    for t in range(len(s)):		#loop across parts of the sentence 
        # print("s2", s)
        # print("s[",t,"]", s[t])
        if s[t][0]==" ":
            s[t]=s[t].strip()	#removing any space in beginning or end
            # print("s[t]2",s[t])
        a.append(s[t].split(" "))
    # print("temp",a)
    for p in a:
    
    #print("z",z)
        for l in stopword:
            for s in p:
                if l==s:
                    ind=p.index(l)
                    p[ind]=" "
        # print("sp4",p)
        res=((" ".join(p)).split("  "))
        # print(len(res))
        for i in range(len(res)):
            res[i]=res[i].strip()
        print(res)
