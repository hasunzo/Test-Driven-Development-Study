##TestCase
class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method();

## WasRun
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)
    def testMethod(self):
        self.wasRun = 1

"""test= WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)"""

##TestCaseTest
class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMehtod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)
TestCaseTest("testMethod").run()