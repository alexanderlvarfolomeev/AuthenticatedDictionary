import unittest
import random
import multidict
import skiplist
import time


class MyTestCase(unittest.TestCase):
    argss = [(random.randint(0, 2), random.randint(0, 100)) for i in range(400000)]

    # def test_skiplist_as_multiset(self):
    #     list = skiplist.SkipList()
    #     lops = [list.contains, list.insert, list.delete]
    #     set = multidict.MultiDict()
    #     sops = [lambda x: str(x) in set, lambda x: set.add(str(x), x), lambda x: None if str(x) not in set else set.pop(str(x))]
    #     for op, c in self.argss:
    #         lres = lops[op](c)
    #         sres = sops[op](c)
    #         # print(lres, sres)
    #         self.assertEqual(lres, sres)
    #         self.assertEqual(len(list), len(set))

    def test_skiplist_as_dictionary(self):
        list = skiplist.SkipList()
        lops = [list.contains, list.insert, list.delete]
        creation = [(random.randint(1, 2), random.randint(0, 100)) for _ in range(10)]
        for op, c in creation:
            list.update(op == 1, c)
        print(list)
        validation = [random.randint(0, 100) for _ in range(1000000)]
        for i in validation:
            print("verify(" + str(i) + ")", list.timestamp)
            response = list.verify(i)
            self.assertEqual(response.validates_against(), True)
            self.assertEqual(list.contains(i), response.subject_contained())

    # def test_list_time(self):
    #     list = skiplist.SkipList()
    #     lops = [list.contains, list.insert, list.delete]
    #     start_time = time.time()
    #     for op, c in self.argss:
    #         lres = lops[op](c)
    #     print("--- list %s seconds ---" % (time.time() - start_time))
    #
    # def test_set_time(self):
    #     set = multidict.MultiDict()
    #     sops = [lambda x: str(x) in set, lambda x: set.add(str(x), x), lambda x: None if str(x) not in set else set.pop(str(x))]
    #     start_time = time.time()
    #     for op, c in self.argss:
    #         sres = sops[op](c)
    #     print("--- set %s seconds ---" % (time.time() - start_time))


def main():
    unittest.main()


if __name__ == '__main__':
    # list = skiplist.SkipList()
    # list.update(True, 47, height=1)
    # list.update(True, 90, height=1)
    # print(list)
    # print(list.verify(92).validates_against())
    main()
