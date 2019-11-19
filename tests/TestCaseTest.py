from src.Run.TestCase import TestCase
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


TestCaseTest("testTemplateMethod").run()

if __name__ == '__main__':
    TestCase.main()
