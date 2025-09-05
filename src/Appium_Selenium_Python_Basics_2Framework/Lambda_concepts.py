"""
A Lambda function is a small anonymous function.
A Lambda function can take any number of arguments, but can only have one expression.

Sytax:  lambda agruments : expression

"""

x = lambda a : a + 10
print(x(5))

x = lambda a,b : a+b+20
print(x(40,50))