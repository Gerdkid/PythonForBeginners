tuple = (1,2,3,4,5)
try:
    tuple.append(6)
except AttributeError as e:
    print('error formed' , e)
else:
    for each in tuple:
        print(each)
        
tuple = (1,2,3,4,5)
try:
    tuple.append(6)
    for each in tuple:
        print(each)
except AttributeError as e:
    print('error formed' , e)
except IOError as e:
    print('file not found' , e)

   