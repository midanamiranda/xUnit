from Run.WasRun import WasRun
from tests.TestResult import TestResult


class ResultListenerTest:
    def testNotification(self):
        self.count = 0
        result = TestResult()
        result.addListener(self)
        WasRun("testMethod").run(result)
        assert 1 == self.count

    def startTest(self):
        self.count = self.count + 1
