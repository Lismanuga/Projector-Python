import random


def generate_random_number():
    return random.randint(1, 100)


for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    filename = char + '.txt'
    with open(filename, 'w') as file:
        random_number = generate_random_number()
        file.write(str(random_number))


with open('summary.txt', 'w') as summary_file:
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        filename = char + '.txt'
        with open(filename, 'r') as file:
            random_number = file.read()
            summary_file.write(f'{filename}: {random_number}\n')
