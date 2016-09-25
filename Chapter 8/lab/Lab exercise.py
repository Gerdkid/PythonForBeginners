string = '1211f3'

def checkType(string):
    string = str(string)
    if(string.isdigit()):
        return "string is a Digit"
    elif(string.isalnum()):
        return "string is Alpha Numeric"
    elif(string == True or string == False):
        return "string is boolean"
    else: 
        return "unknown String type"

print(checkType(string))