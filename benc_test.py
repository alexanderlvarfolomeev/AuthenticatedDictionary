import random
import unittest
import skiplist
import time


class MyTestCase(unittest.TestCase):

    def test_set_time(self):
        list = skiplist.SkipList()
        for i in range(1, 1000001):
            list.update(True, i)
            if i % 100000 == 0:
                start_time = time.time()
                list.update(True, random.randint(1, i))
                print("<--- %s elements --->" % i)
                print("--- 1 insert operation %s seconds ---" % (time.time() - start_time))
                start_time = time.time()
                list.update(False, random.randint(1, i))
                print("--- 1 deletion operation %s seconds ---" % (time.time() - start_time))
                start_time = time.time()
                list.verify(random.randint(1, i))
                print("--- 1 validation operation %s seconds ---" % (time.time() - start_time))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
