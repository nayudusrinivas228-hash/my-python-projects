try:
    file=open('hello.py','r+')
    content1=file.read()
    content=file.writelines('"my name is srinivas iam learning python programming  it is easy to learn and analyse"')
    print(content)
    word=input("search a specif word you want : ")
    if word in content1:
        print(word)
    else:
        print("word not found in the file")
        content1=content1.replace("python","Java")
        print(content1)
except FileNotFoundError as e:
    print("please give the exact file name",e)
finally:
    print("Thank You")



