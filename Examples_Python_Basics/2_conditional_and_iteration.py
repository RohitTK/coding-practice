a, b, c = 10, 20, 30

# If else condition
if a == 10:
    print('a is 10')
    if b == 20:
        print('b is 20')
elif b == 20:
    print('a is not 10 b is 20')
else:
    print('None match')

print('\n----------------------------------------------------------------')

# Single line if
a = 20
b = 10 if a < 10 else 50

print(a, b)

print('\n----------------------------------------------------------------')

# Iterating through a sample list using loops
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Using While
print('\nUsing While:')

cnt = 0

while cnt < len(list1):
    print(list1[cnt], end=', ')
    cnt += 1

# Using For
print('\nUsing For:')

for i in list1:
    print(i, end=' ')

print('\nUsing Range:')

for i in range(10):
    print(list1[i], end=' ')

print('\nUsing enumerate:')
for i, v in enumerate(list1):
    print(f"({i}:{v})", end=', ')

print('\nExample Dict')
dict_var = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

for i in dict_var:
    print(dict_var[i], end=' ')

print('\n')
for v in dict_var.values():
    print(v, end=' ')

print('\n')
for i, v in dict_var.items():
    print(f'{i}: {v}', end=' ')

print('\n----------------------------------------------------------------')

# List comprehension:

print('\nUsing List comprehension:')
l1 = [i for i in range(1, 11)]
print(l1)

l1 = [i for i in range(1, 11) if i % 2 == 0]
print(l1)

print('\n----------------------------------------------------------------')

# Break and continue

print('\nUsing Break:')

for i in range(10):
    if i == 5:
        break
    print(i, end=' ')

print('\nUsing Continue:')

for i in range(10):
    if i == 5:
        continue
    print(i, end=' ')
