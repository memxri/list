colorlist = ['red', 'blue', 'yellow', 'green', 'purple', 'white']
print("You can print one color. Index numbers go from 0 to", len(colorlist) - 1 )
i = int(input("Which color do you want to print "))
while i >= len(colorlist):
    i = int(input("Enter correct number: "))
print(colorlist[i])
