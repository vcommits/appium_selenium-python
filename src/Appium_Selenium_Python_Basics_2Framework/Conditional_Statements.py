####################   Conditional Statements   ####################
"""
--Conditional Statements Conditional statements in Python allow for different blocks of code to be executed depending on whether a condition is true or false. The primary conditional statements are if, elif, and else.
--if statement: Executes a block of code if a condition is true.
--elif statement: Checks an additional condition if the preceding if or elif conditions are false.
--else statement: Executes a block of code if none of the preceding if or elif conditions are true
--Nested if statements: Allow for more complex conditional logic by placing if statements inside other if or else blocks
--Logical operators: Can be used to combine multiple conditions in a single if statement. The and operator returns True if both conditions are true, while the or operator returns True if at least one condition is true.
--Identity Operators "is" "is not"
--Membership Operators "in" "not in"
"""



a =10
b =5
c =10


if a<b:
    print("This is a IF Statement")
elif a>c:
    print("This is an Elif Statement -1")
elif c>b:
    print("This is an Elif STatement -2")
else:
    print("This is a Else Statement")

if a<b:
    if a==c:
        print("A and C are equal")
    else:
        print("This is Else")
else:
    print("This is 1st Else")