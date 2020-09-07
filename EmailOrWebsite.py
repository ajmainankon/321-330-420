#F= open(r"C:\Users\ajmai\Documents\Python\hello.txt", "r")
Text1 = "dilrubashowkat@gmail.com.bd"
Text2 = "www.dilrubashowkat.com"


#This fucntion checks if the passed stuff is from a to z or not
def is_letter(ch):
    if (ch >='a' and ch <= 'z') or (ch >='A' and ch <='Z'):
        return True
    return False

#This fucntion checks if first alphabet is a to z or not
def Validation1(a):
    if is_letter(a[0]):                  
        print ("Text contains a letter")
        return True

#This fucntion checks if there is an @ in the text//derives email or website
def Validation2(a):
    for count in a:
        if count == "@":
            print ("This just might be an Email")
            return True
    return False

#This fucntion checks if all the inputs from \@\ to \.\ is a to z or not 
def Validation1ForEmail(a):
    index1 = a.index("@")
    index2 = a.index('.')
    index_after1 = index1 + 1
    if len(a)> index_after1 and index2:
        rest_of_a = a[index_after1: index2]
        for c in rest_of_a:
            if not is_letter(c):
                return 'invalid'
        return 'Valid'
    return 'invalid'

#This fucntion checks if next alphabet after \.\ is letter or not 
def Validation3ForEmail(a):
    Index1 = a.index(".")
    IndexAfter1 = Index1 + 1
    if len(a)> IndexAfter1:
        if is_letter(a[IndexAfter1]):
            print ("It has a letter after .")
            return
    else:
        print('invalid')
        return

#This fucntion checks if everything after \.\ is letter or not
def Validation4ForEmailAndWebsite(a):
    Index1 = a.index(".")
    IndexAfter1 = Index1 + 1
    lastIndex= len(a)-1
    if len(a)>IndexAfter1:
        mo = a[IndexAfter1: lastIndex]
        for x in mo:
            if not ((is_letter(x)) or (x==".")):
                return False
        return True

#checks if the website address has only letter and \:\ and / before first \.\
def Validation1ForWebsite(a):
    index1 = a.find(".")
    index2 = index1 - 1
    a0 = a[0]
    if len(a)>index2:
        mo = a[0: index1]
        for x in mo:
            if not ((is_letter(x)) or (x==":") or (x=="/")):
                return False
        return True

#checks if the website address has letters or numbers in between two dots
def Validation2ForWebsite(a):
    Index1 = a.index(".")
    IndexAfter1 = Index1 + 1
    lastIndex = len(a)-1 
    mo = a[IndexAfter1: lastIndex]
    Index2 = mo.index(".")
    IndexBefore2 = Index2 - 1 
    if len(mo)>IndexBefore2:
        mosalah = mo[IndexAfter1: IndexBefore2]
        for x in mosalah:
            if not ((is_letter(x)) or (type(x) == int)):
                return False
        return True

#This fucntion checks will act as the run function \\ will do later
def ValidationOfEmailOrWebsite(a):
    Validation1(a)
    if Validation2(a):
        if Validation1ForEmail(a) == "invalid":
            print("Invalid input because there is something else other than a-z after @  ")
        elif Validation4ForEmailAndWebsite(a) == False:
            print ("""This is not an email because it contains alphabet other than a-z or "." after "." yeehaw""")
        elif Validation4ForEmailAndWebsite(a) == True:
            print("This is an Email")
    else:
        if Validation1ForWebsite(a) == True:
            print("""This has only letter or ":" or "/" before first ".""") 
        elif Validation1ForWebsite(a) == False:
            print ("""This does not have only letter and ":" and "/" before first ".""")
            print ("Thus, not a website.")
            return
        if Validation2ForWebsite(a) == True:
            print("This only has letters or numbers in between two dots") 
        elif Validation2ForWebsite(a) == False:
            print("This has smth else other than letters or numbers in between two dots")
            print ("Thus, not a website.")
            return
        if Validation4ForEmailAndWebsite(a) == False:
            print ("""This is not an Website because it contains alphabet other than a-z or "." after "." yeehaw""")
        elif Validation4ForEmailAndWebsite(a) == True:
            print("This is a Website")




ValidationOfEmailOrWebsite(Text2)
#ValidationOfEmailOrWebsite(Text1)





