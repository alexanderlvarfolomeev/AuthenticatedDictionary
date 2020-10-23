import unittest
import random
import multidict
import skiplist
import time
from math import ceil, log2


def int2bytes(item: int) -> bytes:
    return item.to_bytes(ceil(log2(item + 1) / 8), byteorder='big')


class MyTestCase(unittest.TestCase):
    argss = [(random.randint(0, 2), int2bytes(random.randint(0, 100))) for i in range(400000)]

    def test_skiplist_as_multiset(self):
        list = skiplist.SkipList()
        lops = [list.contains, list.insert, list.delete]
        set = multidict.MultiDict()
        sops = [lambda x: str(x) in set, lambda x: set.add(str(x), x), lambda x: None if str(x) not in set else set.pop(str(x))]
        for op, c in self.argss:
            lres = lops[op](c)
            sres = sops[op](c)
            # print(lres, sres)
            self.assertEqual(lres, sres)
            self.assertEqual(len(list), len(set))

    def test_skiplist_as_dictionary(self):
        for _x in range(1000):
            list = skiplist.SkipList()
            creation = [(random.randint(1, 2), int2bytes(random.randint(0, 100))) for _ in range(500)]
            for op, c in creation:
                # print("insert" if op == 1 else "delete", c)
                list.update(op == 1, c)
                # list.validate_tree()
            # print(list)
            validation = [int2bytes(random.randint(0, 100)) for _ in range(100)]
            for c in validation:
                # print("verify(" + str(i) + ")")
                response = list.verify(c)
                self.assertEqual(response.validates_against(), True)
                self.assertEqual(list.contains(c), response.subject_contained())

    def test_list_time(self):
        list = skiplist.SkipList()
        lops = [list.contains, list.insert, list.delete]
        start_time = time.time()
        for op, c in self.argss:
            lops[op](c)
        print("--- list %s seconds ---" % (time.time() - start_time))

    def test_set_time(self):
        set = multidict.MultiDict()
        sops = [lambda x: str(x) in set, lambda x: set.add(str(x), x), lambda x: None if str(x) not in set else set.pop(str(x))]
        start_time = time.time()
        for op, c in self.argss:
            sops[op](c)
        print("--- set %s seconds ---" % (time.time() - start_time))


def main():
    unittest.main()


if __name__ == '__main__':
    # list = skiplist.SkipList()
    # list.update(True, 32, height=1)
    # list.validate_tree()
    # list.update(True, 97, height=1)
    # # list.validate_tree()
    # # list.update(True, 0, height=2)
    # # list.validate_tree()
    # # list.update(True, 5, height=1)
    # # list.update(False, 28)
    # list.validate_tree()
    # print(list)
    # print(list.verify(27).validates_against())
    main()
