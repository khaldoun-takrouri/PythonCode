<<<<<<< HEAD
# new new new

# new new new new

=======
>>>>>>> parent of 38b8711 (new new new)
def add(a,b):
    c = int(input("input num "))
    return a+b+c


print(add(4,9))    


def printName(first,mid,last,age=7):
    print(f"your name is {first} {mid} {last} your age is {age}")


printName(age=8,last="khaldoun",first="jwad",mid="Takrouri")   


def printName(name,*args,**kwargs):
    print(f"your name is {name} ")
    for arg in args:
        print(arg)


#     print(kwargs["d"])    


printName("khaldou","samir","kmal",a="p",d="h") 


# name = input("input name : ")
# if name == "khaldoun":
#     print(f"hi {name}")
# elif name == "m":
#     print(f"Not yet {name}")
# elif name == "t":
#     print(f"Ok {name}")   
# else:
#     print('good bye')         

# def sub():
#     a = float(input("input first num : "))   
#     b = float(input("input second num : "))
#     print(a-b)

# def add():
#     a = float(input("input first num : "))   
#     b = float(input("input second num : ") ) 
#     print(a+b)



# oper = input("input operation + -")
# if oper == "+":
#     add()
# elif oper == "-":
#     sub()   
# 

# a = [1,2,3,4]
# b = [7,8,9]
# c= a[1:3]
# print(c)
# c = a[:3:2]
# print(c)
# a[0]=80
# print(a)
# f=a.index(3)
# print(f)
g = 3 in a
if 3 in a :
    
# print (3 in a)
# b.append(10)

# a.extend(b)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)


# a.pop(1)
# print(a)
# a.remove(4)
# print(a)
# a.pop()
# print(a)

# print(1 in a)

# print(5 in a)
# a.append(1)
# a.append(1)
# print(a)
# print(a.count(1))


# a = {"1":"kh","3":"ta","7":"oi","4":"khgknk"}
# b = {"nnnnnn":"kkkkkk", "dddddd":"aaaaaa"}

#  print(a.get("7"))
# print(a.items())
# for x,y in a.items():
#     print(x ,y)

# # print(a.keys())
# # print(a.values())
# a.popitem()
# print(a)

# a.setdefault("10","murad")
#print(a)
# a["77"] = 8
# print(a)
# a.update(b)
# print(a)


str1 = "khaldoun,Jwad,Takrouri"
# str2 = str1.split(",")
# print(str2)
# print(str1.upper())
# print(str1.lower())
# print(str1[:3])
# print(str1[3])
# print(str1[-1])
# print(len(str1))
# print(str1.index("w"))
# print(str1.replace("u","Q"))
# print(str1.replace("ur","QQ"))
# print(str1.islower())
# print(str1.isupper())
# print(str1.count("u"))

# str3 = str1[::-1]
# print(str3)
# print(str1[::-1])

# for i in range(0,len(str1)-1):
#      print(str1[i])

# str3 = str1[::-1]
# print(str3)

# for i in range(0,len(str3)):
#           print(str3[i])

# print(str3[len(str3)-1])







# class Person:
#     def __init__(self, name):
#         self.name = name

#     def showName(self):
#         print(self.name)


# class Student(Person):
#     def __init__(self, name, age):
#          super().__init__(name)
#          self.age=age

#     def showNameAge(self):
#           print(f"name is {self.name} and age is {self.age}")


# khaldoun = Person("khaldoun Takrouri")
# khaldoun.showName()

# khaldoun1 = Student("khaldsoun",88)

# khaldoun1.showName()
# khaldoun1.showNameAge()



# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

s1 = ["h","e","l","l","o","i","t"]

def reverse_string(str):
    x=0
    y=len(str)-1
    temp=0

    while x<y:
        temp=str[x]
        str[x]=str[y]
        str[y]=temp
        x=x+1
        y=y-1
    return(str)
       
    
new_str = reverse_string(s1)
print(new_str)

# phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


# s4 = "race a car"
s5 = "A man, a plan, a canal: Panama"

def is_palindrome(str):    
    clean_text = ''.join(char for char in str if char.isalnum())
    print(clean_text)
    lower_text = clean_text.lower()
    print(lower_text)
    flag=True
    x=0
    y=len(lower_text)-1

    while x<y:
        if lower_text[x]==lower_text[y]:
            #print(lower_text[x] ,lower_text[y])
            x=x+1
            y=y-1
        else:
            print(lower_text[x] ,lower_text[y])
            flag=False
            break

        
    if flag:
        return True
        
    else:
        return False
        

if is_palindrome(s5):
     print("Output :true")
     print(f"Explanation: s is a palindrome.")
else:
     print("Output :false")
     print(f"Explanation: s is not a palindrome.")    

    
# Word Counter: Create a function that counts the number of words in a sentence. 
# Words are separated by spaces, but you should handle multiple spaces between words.
# Example input: "This is a test sentence with irregular spacing." Expected output: 8    

str5 = "This is a test sentence with irregular spacing.      kk"

def num_of_words(str):
    str6 = str5.split(" ") 
    str7 = []

    for w in str6:
        if w != "":
            str7.append(w)

    return str7  


print(f"This sentence has {len(num_of_words(str5))} words ")
