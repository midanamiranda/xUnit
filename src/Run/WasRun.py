from Run.TestCase import TestCase


class WasRun(TestCase):

    def __init__(self, name):
        TestCase.__init__(self, name)
        self.log = ""

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown"

    def testBrokenMethod(self):
        raise Exception
