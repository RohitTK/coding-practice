# # datatypes
# int_var = 10
# float_var = 10.23
#
# bool_var = True
#
# string_var1 = 'Hello World'
# string_var2 = "Hello World"
# string_var3 = """Hello
# World"""
#
# string_var4 = string_var1 + ' ' + str(int_var) + ' ' + str(float_var)
# string_var5 = f"{string_var1} {int_var} {float_var}"
#
#
# print(int_var, float_var, string_var1, string_var2, bool_var)
# print('\nConcat:', string_var4, '| f string:', string_var5)

# string_var6 = "C:\\Documents\\nodejs_scripts"
# string_var7 = r"C:\Documents\nodejs_scripts"
# print('\nWithout r:', string_var6, '| r string:', string_var7)

# Unpacking
# int_var1, float_var1, string_var1 = 99, 99.99, 'Bye World'
#
# print(int_var1, float_var1, string_var1)
#
# print('\n----------------------------------------------------------------')

list_var1 = [1, 2, 3, 4]
list_var2 = [1, 'abc', 10.30]
list_var3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 5]]

tuple_var = (1, 2, 3, 4)
set_var = {'string1', 'string2', 'string3', 'string3'}
dict_var = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

print('List:', list_var1, 'elements:', list_var1[0], list_var1[-1])
print('List Slicing:', list_var1[:3], list_var1[1:3], list_var1[-3:-1])
print('List Slicing with step:', list_var1[::2])

print('\nList:', list_var2)
print('List:', list_var3, 'elements:', list_var3[1][2], list_var3[-1][1])

print('\nTuple:', tuple_var, 'elements:', tuple_var[0], tuple_var[-1])
print('Set:', set_var)

print('Dict:', dict_var, 'elements:', dict_var['key3'], dict_var.get('key6'))

print('\n----------------------------------------------------------------')

# String functions
sample_str = 'hello world'
print(sample_str + sample_str)
print(sample_str * 5)
print(len(sample_str))
print(sample_str.upper())
print(sample_str.capitalize())
print(sample_str.replace('hello', 'bye'))


print('\n----------------------------------------------------------------')

# List functions
sample_list = [1, 2, 3, 4, 5]
print(max(sample_list))
print(min(sample_list))
print(sum(sample_list))

sample_list.append(6)
print(sample_list)

sample_list.sort(reverse=True)
print(sample_list)

sample_list.pop()
print(sample_list)

sample_list.remove(3)
print(sample_list)

sample_list.append([7, 8, 9])
print(sample_list)
sample_list.extend([7, 8, 9])
print(sample_list)

sample_list = ['1', '2', '3', '4', '5']
print(", ".join(sample_list))
print('\n----------------------------------------------------------------')
