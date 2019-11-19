from unittest import TestCase
from src.Run.WasRun import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown" == test.log)

    def tearDown(self):
        pass

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 1 failed", result.summary)


if __name__ == '__main__':
    TestCase.main()
