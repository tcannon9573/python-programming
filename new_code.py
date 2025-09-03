# create alist using concise expression
num = input("Enter a number: ")
my_list = [x**2 for x in range(int(num)+1)]

print(my_list)
