# Converting Data Types between one another

e = 3.4
print(e)
print(type(e))

print("=========================")

#   Cast floating point number to an integer
d = int(e)
print(d)
print(type(d))

print("=========================")


#   Cast integer to string
d = str(e)
print(d)
print(type(d))

print("=========================")


#   Cast string to complex
d = complex(e)
print(d)
print(type(d))


print("=========================")


#   Convert String to List targeting a "," as the delimiter

comma_wordlist = "python, ruby, java, C++, javascript, swift, kotlin"
wordlist = comma_wordlist.split(',')
print(comma_wordlist)
print(type(wordlist))


print("=========================")
#   Convert String to List targeting whitespace as the delimiter

comma_wordlist = "jack diane brady colston ruby lainey"
wordlist = comma_wordlist.split( )
print(comma_wordlist)
print(type(wordlist))


print("=========================")
#   Convert String to List Spliting each word in a string

wordchew = "The first method to convert a string to a list in Python is the split() method"
chew = wordchew.split( )
print(chew)
print(type(wordchew))


print("=========================")
#   Convert a String using List Comprehension

poetry = "In the burned house I am eating breakfast."
letterstorm = [char for char in poetry]
print(letterstorm)
print(type(letterstorm))
print(letterstorm[9])


print("=========================")
#   Convert a String using ast.literal_eval() Function

import ast
let_string = "['body', 'mind', 'spirit', 'soul']"
conv = ast.literal_eval(let_string)
print(conv)
print(type(conv))