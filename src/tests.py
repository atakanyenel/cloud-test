from TestSuite import TestSuite
import System
from time import sleep


@TestSuite.test
def TestAdd():
    sleep(10)
    assert (System.add(1, 2) == 3)
    assert (System.add(0, 0) == 0)
    assert (System.add(-1000, 900) == -100)


@TestSuite.test
def TestSubtract():
    assert (System.subtract(4, 5) == -1)
    assert (System.subtract(2, 1) == 1)
    assert (System.subtract(-1000, -1000) == 0)


@TestSuite.test
def TestFail():
    sleep(5)
    assert (1 == 2)


print(*TestSuite.getTests(), sep="\n")

TestSuite.run()

print(*TestSuite.getTests(), sep="\n")
