import re
F= open("/content/hello.txt", "r")

lines= F.read()
mystr1 = lines.split()
# mystr = '\t'.join([line.strip() for line in lines])
# mystr1 = mystr.replace(" ", "")
# for word in mystr1:
#     if re.search("add", word):
#         a = mystr1.index(word)
#         print (word, a)
# print (mystr1) 
myStack = []
regEx = "[public| private|] [static]? [void|int|String|double] [a-z]([a-z]*[0-9]*)"
rType = "(int|double|String)"
for input in mystr1:
    myStack.append(input)
    if re.search("public", input):
        print(myStack.pop())
    # else re.search
        