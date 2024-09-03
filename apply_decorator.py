def apply_decorator(func):
    def inner():
        print("Decorator Applied")
        return func()
    return inner

@apply_decorator
def decoratade():
    print("Wambua")

decoratade()