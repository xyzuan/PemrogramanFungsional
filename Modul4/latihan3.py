def title_decorator(function):
    def wrapper():
        func = function()
        make_title = func.title()
        print(make_title + " " + "- Data is convert to title case")
        return make_title
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        print(str(splitted_string) + " " + "- Then Data is splitted")
        return splitted_string
    return wrapper


def main():
    @split_string
    @title_decorator
    def say_hi():
        return 'hello there'
    say_hi()

if __name__ == "__main__":
    main()