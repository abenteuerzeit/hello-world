def get_hello_message(name):
    if not name:
        name = "World"
    return f"Hello, {name}!"


def get_user_name():
    name = input("What's your name?: ")
    return name.capitalize()


def say_hello():
    hello = get_hello_message(get_user_name())
    print(hello)


say_hello()