def add(v,b):
    print(v+b)

# add(7,5)

def vb(g,h):
    print('ffdf')
    add(g,h)
    print('hhhh')

vb(7,8)



def div(x,y):
    print(x/y)

def outer_fun(func):
    # print(func)
    def inner(x,y):
        if x < y:
            x,y= y,x
            r = func()
            return r
        r = func()
        return r
    return inner

outer_fun(div(7,8))


def devide(x, y):
    # print(x / y) #due to this I encounter with none
    return x/y

def outer_div(func):  # Single argument
    def inner(k, j):  # Double argument
        if k < j:
            k, j = j, k  # Swap k and j if k is less than j
        r = func(k,j)  # Call the original function with swapped arguments
        return r  # Return the result of the original function

    return inner

div1 = outer_div(devide)  # Create a modified version of devide using outer_div decorator
result = div1(40, 4)  # Call the modified version with arguments (4, 40)
print(result)


def deco(func):  # Single argument
    def inner(k, j,l,r=10):  # Double argument
        if k > j:
            k, j = j, k  # Swap k and j if k is less than j
        r = func(k,j) # Call the original function with swapped arguments
        return r  # Return the result of the original function

    return inner

# @deco
# def add(x,y):
#     return x + y

@deco
def min(x,y):
    return y-x

print(min(5,6,5))



def smaert_dev(func):
    def inner(x, y):
        print("I'm going to divide", x, "and", y)
        if y == 0:
            print("Not possible")
            return "xxxxxxxxxx"
        return func(x, y)

    return inner

@smaert_dev
def devi(x, y):
    if y == 0:
        return "xxxxxxxxxx"
    result = x / y
    print(result)
    return result

result = devi(60, 0)
print(result)




