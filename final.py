#Create a citylist
citylist = ['Bangkok','Nakhon Ratchasima','Tokyo','Nan','Trat']

#Traverse the city
for i in range(len(citylist)):
    print(citylist[i])

#Append the city
name = input("Add a new city: ")
citylist.append(name)

#Delete a city
delete = int(input("Which city do you want to delete?: "))
del citylist[delete]

#print the citylist
print(citylist)