football_team = []

for i in range(11):
    name = input("Add a player in the football team: ")
    football_team.append(name)
print(football_team)

repeat = 'Y'
while repeat == 'Y':
    print(football_team)
    final_index = len(football_team)
    print("You can print any name from the list. Index numbers go from 0 t0", final_index)
    i = int(input("Which name do you want to change?: "))
    while i >= len(football_team):
        i = int(input("Enter correct number: "))
    football_team[i] = int(input("Enter a new name: "))
    print(football_team)

    print("You can print any name from the list. Index numbers go from 0 t0", final_index)
    i = int(input("Which name do you want to delete?: "))
    while i >= len(football_team):
        i = int(input("Enter correct number: "))
    del football_team[i]
    print(football_team)
    repeat = input("Do you want to edit or delete name? (Y/N)")
