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
        self.tearDown()
        return TestResult()

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

    def tearDown(self):
        self.log= self.log + "tearDown "

## TestResult
class TestResult:
    def summary(self):
        return "1 run, 0 failed"

## TestCaseTest
class TestCaseTest(TestCase):
    def setUp(self):
        self.test= WasRun("testMethod")

    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown " == test.log)

    def tearDown(self):
        pass

    def testResult(self):
        test = WasRun("testMethod")
        result= test.run()
        assert ("1 run, 0 failed" == result.summary())

TestCaseTest("testTemplateMethod").run()