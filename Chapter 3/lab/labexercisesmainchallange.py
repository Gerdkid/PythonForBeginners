a = 1
b = 0
c = 1

if(b == 1):
    bHolder = 0
elif(b==0):
    bHolder = 1
    
if(a == 1 and bHolder == 1):
    firstBracketHolder = 1
else:
    firstBracketHolder = 0
if(firstBracketHolder == 1 or c == 1):
    print('Q = 1')
else:
    print('Q = 0')