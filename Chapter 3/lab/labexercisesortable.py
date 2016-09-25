a = 1
b = 0

if (a == 1 and b == 1):
    print('1')
elif ((a == 1 and b == 0) or (a == 0 and b == 1)):
    print('1')
elif (a == 0 and b ==0):
    print('0')
else:
    print('Invalid Input')
