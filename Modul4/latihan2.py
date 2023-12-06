def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

def main():
    @uppercase_decorator
    def say_hi():
        return 'hello there'
    
    print(say_hi())

if __name__ == "__main__":
    main()