import random
import unittest
import skiplist
import time
import math
import matplotlib.pyplot as mlp


def int2bytes(item: int) -> bytes:
    return item.to_bytes(math.ceil(math.log2(item + 1) / 8), byteorder='big')


class MyTestCase(unittest.TestCase):
    benches = [[], [], []]

    def test_set_time(self):
        list = skiplist.SkipList()
        for i in range(1, 1000001):
            list.update(True, int2bytes(i))
            if i % 100000 == 0:
                print("<--- %s elements --->" % i)
                ints = [int2bytes(random.randint(1, i)) for _ in range(1000)]
                start_time = time.time()
                for j in ints:
                    list.update(True, j)
                t = (time.time() - start_time)
                self.benches[0].append(t)
                print("--- 1 insert operation %s ms ---" % t)
                start_time = time.time()
                for j in ints:
                    list.update(False, j)
                t = (time.time() - start_time)
                self.benches[1].append(t)
                print("--- 1 deletion operation %s ms ---" % t)
                start_time = time.time()
                for _ in range(1000):
                    list.verify(int2bytes(random.randint(1, i)))
                t = (time.time() - start_time)
                self.benches[2].append(t)
                print("--- 1 validation operation %s ms ---" % t)
        xs = [i * 100000 for i in range(1, 11)]
        fig = mlp.figure(figsize=(16, 9))
        mlp.scatter(xs, self.benches[0], s=6 ** 2, marker='^', label='insertion')
        mlp.scatter(xs, self.benches[1], s=6 ** 2, marker='o', label='deletion')
        mlp.scatter(xs, self.benches[2], s=6 ** 2, marker='s', label='query')
        mlp.xlabel('number of elements', fontsize=14, fontweight='bold')
        mlp.ylabel('average time (ms)', fontsize=14, fontweight='bold')
        mlp.legend(fontsize=14)
        mlp.savefig('result.png')
        fig.show()


def main():
    unittest.main()


if __name__ == '__main__':
    main()
