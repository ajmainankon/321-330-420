import re
F= open("notepad.txt", "r")
list1= []
list2= []
lines= F.read()
mystr1 = lines.split('\n')
regex = "[\x55/][\x67][\x74][1][0]" 
for password in mystr1:
    line = re.search("[\x55/][\x67][\x74][1][0]", list)
    print(line)
#     if len(password) == 6:
#         list1 = password[0: -1]
#         print (list1)
# for letter in list1:
#     if letter(0) == "U":
#         list2 = letter [0: -1]
#         print (list2)
                # for ASCII in letter:
                    
                # print ("ye")
        # print ("ya")
# for p in mystr1:
#     print(p)


#still not finished