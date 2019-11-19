from tests.TestResult import TestResult


class TestCase:

    def __init__(self, name):
        self.name = name

    def setUp(self, name):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        exec "self." + self.name + "()"
        self.tearDown()
        return result

    def tearDown(self):
        pass
