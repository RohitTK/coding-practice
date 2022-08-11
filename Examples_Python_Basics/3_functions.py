def fun(num):
    if num % 10 == 0:
        print('Divisible by 10')
        return 1
    else:
        print('Not Divisible by 10')
        return -1


print(fun(10))
print(fun(23))


def fun1(num: int) -> int:
    if num % 10 == 0:
        print('Divisible by 10')
        return 1
    else:
        print('Not Divisible by 10')
        return -1


print(fun1(10))
print(fun1(23))

print('\n----------------------------------------------------------------')


# Default Parameters:
def oFun1(a,b=10):
    print('Var1:', a, 'Var2:', b)


oFun1(1)
oFun1(1, 2)

print('\n----------------------------------------------------------------')


# Calling Function in a function:
def fun1():
    print('Hello ', end='')


def fun2():
    # def fun1():
    #     print('Hello ', end=' ')

    fun1()
    print('World')


fun2()
