from tests.TestResult import TestResult


class TestCase:

    def __init__(self, name):
        self.name = name

    def setUp(self, name):
        pass

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            exec "self." + self.name + "()"
        except:
            result.testFailed()
        self.tearDown()

    def tearDown(self):
        pass
