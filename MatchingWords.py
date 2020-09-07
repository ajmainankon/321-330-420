import re
# F= open(r"/content/hello.txt", "r")
a = "[a-c]{3}cab+(da)*f,db*a[^def](2)gh,def[k-p]*p+"

i = "defkmnpmpp,acbcabbf,pqrstdd,dbaabggh,dbbbbamkgh"

pattern = a.split(",")
line= i.split(",")

# print(pattern)
# print(line)

def run(line, pattern):
    result = []
    i = 0
    for word in line:
        for pat in pattern:
            z = re.match(pat, word)
            if z:
                result.append(word)
                print("Yes Match, " + word + "   for   " + pat)      
                i = i+1  
            else:
                
                print("NO Match, " + word + "   for   " + pat)
              
    # for i in result:
    #     print("YES, ")
    # print(result)
            
run(line, pattern)

# def result(pattern, test_line):
#     result = re.match(pattern, test_line)
#     if result:
#         print("Search successful. YES." + test_line )
#     else:
#         print("Search unsuccessful.")

#result(a1, b1)

