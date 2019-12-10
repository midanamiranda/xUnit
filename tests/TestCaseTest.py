from unittest import TestCase

from src.Run.WasRun import WasRun
from tests.TestResult import TestResult
from tests.TestSuite import TestSuite


class TestCaseTest(TestCase):

    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert ("setUp testMethod tearDown" == test.log)

    def tearDown(self):
        pass

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert ("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert ("1 run, 1 failed", self.result.summary())

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert ("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        new_suite = TestSuite()
        new_suite.add(WasRun("testMethod"))
        new_suite.add(WasRun("testBrokenMethod"))
        new_suite.run(self.result)
        assert ("2 run, 1 failed" == self.result.summary())


if __name__ == '__main__':
    suite = TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testSuite"))
    result = TestResult()
    suite.run(result)
    print result.summary()
