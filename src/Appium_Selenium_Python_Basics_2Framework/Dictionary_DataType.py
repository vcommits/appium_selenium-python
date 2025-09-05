"""
-Dictionaries are key and value pairs, written in curly brackets "{}"

Ex :

    employeeData = {
    "name": "Day"
    "number": "95953333"
    "DOB": 1990
}


"""


#   Create a Dictionary
employeeData={
    "name":"Day","number":987632111,"DOB":1900}
print(type(employeeData))
print(employeeData)




#   Access values from a Dictionary
a=employeeData["number"]
print(a)

#   Update or change Dictionary values
employeeData["name"] ="Vince"
print(employeeData)

#   Add key and value pairs for existing Dictionaries
employeeData["address"]="USA"
print(employeeData)

#   Get the length of a Dictionary
print(len(employeeData))

#   Copy Dictionaries to variables
emp = employeeData.copy()
print(emp)

#   Iterate values in a Dictionary
for b in employeeData.keys():
    print(employeeData[b])

#   Iterate both keys and values
for c,d in employeeData.items():
    print(c,d)


#   Remove Dictionary values
employeeData.pop("address")
print(employeeData)



#   Clear a Dictionary
employeeData.clear()
print(employeeData)



#   Delete and validate a Dictionary
del employeeData
print(employeeData)