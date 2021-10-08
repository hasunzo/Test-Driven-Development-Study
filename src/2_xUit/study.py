## TestCase
class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

## WasRun
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun= None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun= 1
        self.log= self.log + "testMethod "

    def setUp(self):
        self.wasRun= None
        self.wasSetUp= 1
        self.log= "setUp "

## TestCaseTest
class TestCaseTest(TestCase):
    def setUp(self):
        self.test= WasRun("testMethod")

    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run()
        assert ("setUp testMethod " == test.log)

TestCaseTest("testTemplateMethod").run()