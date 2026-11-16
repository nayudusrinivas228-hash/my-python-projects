file=open("hello.py","r")
content=file.read()
count=content.split()
lines = content.splitlines()
word=len(count)
words=len(lines)
print('Number of words are there in the txt file is :',word)
print('Number of lines are there in the file is  : ',words)

