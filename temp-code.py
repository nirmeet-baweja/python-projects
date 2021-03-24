# def mylen(p, n):
#     if p == []:
#         return n
#     else:
#         return mylen(p[1:], n+1)


# print(mylen([1, 2, 3, 4, 5, 6], 5))
# str = "t"
# print(str[1:])
# print(mylen("Text", 1))


def myleni(p, n):
    temp_p = p[:]
    result = n
    while temp_p != []:
        result = result+1
        temp_p = temp_p[1:]
    return result


# print("iterative method")
# print(myleni([1, 2, 3, 4, 5, 6], 5))


def sum_even(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i
    return total


def sum_evenr(n):
    if(n <= 0):
        return 0

    if(n == 2):
        return 2
    elif (n % 2 == 0):
        return n + sum_evenr(n-2)
    else:
        return n + sum_evenr(n-1)


def sum_evenr2(n):
    if(n <= 0):
        return 0

    if(n == 2 | n == 3):
        return 2
    elif (n % 2 == 0):
        return n + sum_evenr(n-2)


print("iterative")
print(sum_even(-10))
print("recursive 1")
print(sum_evenr(-10))
print("recursive 2")
print(sum_evenr2(-10))


def min(t):
    m = 0
    for i in t:
        if i < m:
            m = i
    return m


def min_recursive(t, n):
    if t == []:
        return n
    elif t[0] < n:
        return max(t[1:], t[0])
    else:
        return max(t[1:], n)


def max(k, n):
    if k == []:
        return n
    elif k[0] > n:
        return max(k[1:], k[0])
    else:
        return max(k[1:], n)


def max_iterative(k):
    n = 0
    for i in k:
        if i < n:
            n = i
    return n


def sum_odd(n, total):
    if n == 1:
        return total
    elif n % 2 == 0:
        return sum_odd(n - 1, total)
    else:
        return sum_odd(n - 2, total + n)


def sum_odd_iterative(n):
    total = 0
    print("n is ")
    print(n)
    for i in range(3, n+1, 2):
        print(i)
        total += i
    return total


print(sum_odd(10, 0))
print("iterative")
print(sum_odd_iterative(10))

# fn = 1 for n=1, and 2*f(n-1)+1 for n>1


def fn_recursive(n):
    if n == 1:
        return 1
    elif n > 1:
        return 2*fn_recursive(n-1)+1


def fn_iterative(n):
    result = 1
    for i in range(0, n):
        result *= 2 + 1
    return result


print("ouput of recursive function")
print(fn_recursive(5))
print("ouput of iterative function")
print(fn_iterative(5))


def fn2_iterative(n):
    result = 1
    for i in range(1, n):
        result += 2
    return result


print("fn 2")
print(fn2_iterative(3))

# fn 2^n


def exponent_2(n, prod):
    if n == 0:
        return prod
    elif n > 0:
        return exponent_2(n-1, 2*prod)
    else:
        return exponent_2(n+1, 0.5*prod)


print("test exponent 2")
print(exponent_2(-4, 1))

# define intToBin - for changing integer to binary


def intToBin(num, result):
    if num == 0:
        return (result + '0')[::-1]
    elif num == 1:
        return (result + '1')[::-1]
    else:
        print(str(num % 2))
        return intToBin(num//2, result + str(num % 2))


print("Testing intToBin function")
print(intToBin(10, ''))
