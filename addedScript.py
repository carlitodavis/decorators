def check_input(func):
    def wrapper(value):
        if value < 0:
            print("Error: Value must be a positive number.")
            return None
        return func(value)
    return wrapper

@check_input
def square_root(num):
    return num ** 0.5

print(square_root(49))
print(square_root(-16)) 