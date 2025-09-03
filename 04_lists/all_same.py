#get list
n = int(input("Enter the number of elements: "))

elements = []
while n:
    elements.append(int(input()))
    n -= 1

print(elements)

#check if all the elements are equal
# print true
#otherwise false

if len(elements) < 2:
    print(bool(True))
else:
    #Finish it at home
    