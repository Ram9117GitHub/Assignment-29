"""Write a Python script to count the number of Python keywords occurring in a python source file."""
count_word = 0
with open('cities.txt','r') as f:
    data = f.read()
    lines = data.split()
    count_word+=len(lines)
print(count_word)
