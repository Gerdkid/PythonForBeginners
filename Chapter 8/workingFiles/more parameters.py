list1 = [1,2,3,4]

def function_name(lists):
    "This will simply demostrate by reference"
    lists.append([5,6,7,8]);
    print("This is the value:",lists)
    return

print("The values are",list1)
function_name(list1)
print("This is the value:",list1)