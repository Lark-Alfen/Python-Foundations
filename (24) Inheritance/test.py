class test:
    def __init__(self, name):
        self.name = name

    def intro(self):
        return f"My name is {self.name}"


t = test("Alice")
x=t.intro()
print(x)
