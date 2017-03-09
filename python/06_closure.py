# object with state
class PyconPrinter():
    def __init__(self, prefix="pycon:"):
        self.prefix = prefix
    def __call__(self, msg):
        print(self.prefix, msg)

pp = PyconPrinter()
pp("Hi all from regular object")

# closure
def pycon_printer(prefix="pycon:"):
    def pycon_print(msg):
        print(prefix, msg)
    return pycon_print

p = pycon_printer()
p("Hi all from closure")


