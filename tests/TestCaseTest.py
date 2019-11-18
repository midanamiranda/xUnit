from src.Run.TestCase import TestCase
from src.Run.WasRun import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert (not test.wasRun)
        test.run()
        assert test.wasRun


TestCaseTest("testRunning").run()

if __name__ == '__main__':
    TestCase.main()