import random
import unittest
import skiplist
import time
import math


def int2bytes(item: int) -> bytes:
    return item.to_bytes(math.ceil(math.log2(item + 1) / 8), byteorder='big')


class MyTestCase(unittest.TestCase):

    def test_set_time(self):
        list = skiplist.SkipList()
        for i in range(1, 1000001):
            list.update(True, int2bytes(i))
            if i % 100000 == 0:
                ints = [int2bytes(random.randint(1, i)) for _ in range(100)]
                start_time = time.time()
                for j in ints:
                    list.update(True, j)
                print("<--- %s elements --->" % i)
                print("--- 1 insert operation %s seconds ---" % ((time.time() - start_time) / 100))
                start_time = time.time()
                for j in ints:
                    list.update(False, j)
                print("--- 1 deletion operation %s seconds ---" % ((time.time() - start_time) / 100))
                start_time = time.time()
                for _ in range(100):
                    list.verify(int2bytes(random.randint(1, i)))
                print("--- 1 validation operation %s seconds ---" % ((time.time() - start_time) / 100))


def main():
    unittest.main()


if __name__ == '__main__':
    main()