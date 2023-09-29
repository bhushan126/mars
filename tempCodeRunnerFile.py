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