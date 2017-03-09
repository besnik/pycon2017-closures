# closure used as decorator

def counter(func):
    count = 0
    def inc_count(*args, **kwargs):
        print("Calling", func.__name__)
        func(*args, **kwargs)
        nonlocal count
        count += 1
        print("        Called", count, "times")
    return inc_count

@counter
def follow():
    print("    Follow Freeman")

follow()
follow()
follow()

