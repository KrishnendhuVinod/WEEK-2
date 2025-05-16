# filename: numbers_output.py
with open('numbers.txt', 'w') as file:
    for i in range(1, 101):
        file.write(str(i) + '\n')
print("Numbers from 1 to 100 have been written to 'numbers.txt' file.")
