for data in [1,2,3,4,5]:
    print(data)
    
for data in 'string':
    print(data)
    
for key,data in enumerate('string'):
    if key % 2 == 0:
        print('The letter {} is in an even location'.format(data))
        