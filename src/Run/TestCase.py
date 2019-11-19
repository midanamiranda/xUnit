class TestCase:

    def __init__(self, name):
        self.name = name

    def setUp(self, name):
        pass

    def run(self, result):
        result.testStarted()
        self.setUp()
        exec "self." + self.name + "()"
        self.tearDown()
