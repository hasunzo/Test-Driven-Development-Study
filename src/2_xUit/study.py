## TestCase
class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()

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

    def testBrokenMethod(self):
        raise Exception

## TestResult
class TestResult:
    def __init__(self):
        self.runCount= 0
        self.failureCount= 0

    def testFailed(self):
        self.failureCount= self.failureCount + 1

    def testStarted(self):
        self.runCount= self.runCount + 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failureCount)

## TestSuite
class TestSuite:
    def __init__(self):
        self.tests= []      ## 빈 컬렉션 생성

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)

## TestCaseTest
class TestCaseTest(TestCase):
    def setUp(self):
        self.result= TestResult()

    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run(self.result)
        assert ("setUp testMethod tearDown " == test.log)

    def tearDown(self):
        pass

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test= WasRun("testBrokenMethod")
        test.run(self.result)
        assert ("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        self.result.testStarted()    ## 테스트가 시작할 때 보낼 메시지
        self.result.testFailed()     ## 테스트가 실패할 때 보낼 메시지
        assert ("1 run, 1 failed" == result.summary())

    def testSuite(self):
        suite= TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert ("2 run, 1 failed" == result.summary())

suite= TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))
result= TestResult()
suite.run(result)
print(result.summary())