#create a list of strings

myList = []

for i in range(10):
    word = input("Enter the {}° String: ".format(i))
    myList.append(word)

print (myList)