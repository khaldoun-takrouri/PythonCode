
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

s1 = ["h","e","l","l","o","i","t"]
s4=""
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

    return str
       
    
new_str = reverse_string(s4)
print(new_str)

print("*******************************************************************")

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
    #print(lower_text)
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
    # yes
        
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

print("*******************************************************************")

# Word Counter: Create a function that counts the number of words in a sentence. 
# Words are separated by spaces, but you should handle multiple spaces between words.
# Example input: "This is a test sentence with irregular spacing." Expected output: 8    

str5 = "This is a test sentence with irregular spacing.      kk"

def num_of_words(str):
    str6 = str.split(" ") 
    str7 = []

    for w in str6:
        if w != "":
            str7.append(w)

    return str7  


print(f"This sentence has {len(num_of_words(str5))} words ")


print("*******************************************************************")    

str = ""
char11 = "khaldoun : ta"

for char in char11: 
   if char.isalnum():
       str = str + char

print(str)   

print("wow")