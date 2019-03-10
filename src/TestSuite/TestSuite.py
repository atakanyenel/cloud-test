import logging
from .server import server
from threading import Thread
import time
_Tests = []


def test(func):
    """register function to test suite"""
    _Tests.append(_Test(func))


def run():
    """Run the test suite"""
    print("Test Suite runner called")
    thread = Thread(target=server.start)  # Python threads
    thread.start()
    for t in _Tests:
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
        self.elapsed = 0

    def __repr__(self):
        return f"{self.name} : {self.status}  in {self.elapsed:.4f}"

    def run(self):
        self.status = self.RUNNING
        start_time = time.perf_counter()
        try:
            self.function()
            self.status = self.PASS
        except AssertionError:
            logging.error(
                "There is an error in test:", exc_info=True)
            self.status = self.FAIL
        finally:
            end_time = time.perf_counter()
            self.elapsed = end_time-start_time
