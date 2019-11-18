class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        exec "self." + self.name + "()"
