colors = []

while True:
    color = input('Enter a color: ')
    if color == 'done':
        break
    colors.append(color)

for color in colors:
    print(color)
