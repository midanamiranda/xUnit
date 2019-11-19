from Run.TestCase import TestCase


class WasRun(TestCase):

    def setUp(self):
        self.log = "setUp"

    def testMethod(self):
        self.log = self.log + "testMethod"

    def tearDown(self):
        self.log = self.log + "tearDown"

