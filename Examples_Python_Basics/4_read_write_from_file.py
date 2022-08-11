import os

print(os.getcwd())

data = {}

with open('sample.txt', 'r') as f, open('sample_output.txt', 'w') as w:
    for line in f:
        key, value = line.split(', ')
        data[key] = value.replace('\n', '')
        w.write(f'{key}: {value}')

print(data)

print(data["key1"])
