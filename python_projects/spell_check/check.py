from textblob import TextBlob
file1=open("file.txt")
a=file1.read()


print("original text : ",str(a))


b=TextBlob(a)

print("corrected text : "+str(b.correct()))


file1.close()
d=open("corrected.txt","w")
d.write(str(b.correct()))
d.close()

