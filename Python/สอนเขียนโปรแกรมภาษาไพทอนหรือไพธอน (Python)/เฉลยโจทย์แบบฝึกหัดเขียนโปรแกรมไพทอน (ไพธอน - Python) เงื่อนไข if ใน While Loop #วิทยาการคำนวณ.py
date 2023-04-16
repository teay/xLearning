passengers = {}
total_weight = 0

while True:
    name = input('What is your name? ')
    if not name:
        break
    weight =int(input('What is your weight '))

    if total_weight + weight < 1000:
        passengers[name] = weight
        print(f'Welconme {name}. You can board the ship.')
        # total_weight = total_weight + weight
        total_weight += weight
    else:
        print(f'Sorry {name}. You cannot board the ship.')
print('All passsengers are', passengers)