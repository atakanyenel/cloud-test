import logging
from .server import server
from threading import Thread
_Tests = []


def test(func):
    """register function to test suite"""
    _Tests.append(_Test(func))


def run():
    """Run the test suite"""
    print("Test Suite runner called")
    thread = Thread(target=server.start)  # Python threads
    thread.start()
    for t in _Tests:  # TODO: do we want to run parallel or not
        thread = Thread(target=t.run).start()


def getTests():
    return _Tests


class _Test():
    WAITING = "Queued"
    RUNNING = "Running"
    SKIP = "Skipped"
    PASS = "Passed"
    FAIL = "Failed"

    def __init__(self, function):
        self.function = function
        self.name = function.__name__
        self.status = self.WAITING

    def __str__(self):
        return "%s : %s" % (self.name, self.status)

    def __repr__(self):
        return self.__str__

    def run(self):
        self.status = self.RUNNING
        try:
            self.function()
            self.status = self.PASS
        except AssertionError:
            logging.error(
                "There is an error in test:", exc_info=True)
            self.status = self.FAIL
