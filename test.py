import pytest
import random
import skiplist
import multidict
import time


def setup_module(module):
    pass


def made_n_list(n: int):
    skip_list = skiplist.SkipList()
    for i in range(n):
        skip_list.update(True, i)
    return skip_list


def made_rand_n_list(n: int):
    skip_list = skiplist.SkipList()
    multiset = multidict.MultiDict()
    for _ in range(n):
        rand_num = random.randint(0, n * 2)
        multiset.add(str(rand_num), "")
        skip_list.update(True, rand_num)
    return [skip_list, multiset]


def test_skiplist_update_insert():
    skip_list = made_n_list(1000)
    for _ in range(100):
        rand_num = random.randint(0, 2000)
        assert skip_list.contains(rand_num) == (rand_num < 1000)


def test_skiplist_update_insert_random():
    skip_list, multiset = made_rand_n_list(1000)
    assert skip_list.__len__() == multiset.__len__()
    for _ in range(300):
        rand_num = random.randint(0, 1500)
        assert skip_list.contains(rand_num) == multiset.__contains__(str(rand_num))


def test_skiplist_update_delete():
    skip_list = made_n_list(1000)
    for i in range(500, 1000):
        skip_list.update(False, i)
    for _ in range(100):
        rand_num = random.randint(0, 1000)
        assert skip_list.contains(rand_num) == (rand_num < 500)


def test_skiplist_update_delete_random():
    skip_list, multiset = made_rand_n_list(1000)
    for i in range(500):
        rand_num = random.randint(0, 1500)
        skip_list.update(False, rand_num)
        if multiset.__contains__(str(rand_num)):
            multiset.pop(str(rand_num))
    for i in range(300):
        rand_num = random.randint(0, 1500)
        assert skip_list.contains(rand_num) == multiset.__contains__(str(rand_num))


def test_verify():
    skip_list = made_n_list(1500)
    validation = [random.randint(0, 3000) for _ in range(100)]
    for i in validation:
        response = skip_list.verify(i)
        assert response.validates_against()
        assert response.subject_contained() == (i < 1500)


def test_verify_random():
    skip_list, multiset = made_rand_n_list(1500)
    validation = [random.randint(0, 3000) for _ in range(150)]
    for i in validation:
        response = skip_list.verify(i)
        assert response.validates_against()
        assert response.subject_contained() == multiset.__contains__(str(i))


def common_test(n, m):
    skip_list, multiset = made_rand_n_list(n)
    argss = [(random.randint(0, 2), random.randint(0, 10000)) for _ in range(m)]
    lops = [lambda x: skip_list.verify(x).subject_contained(),
            lambda x: skip_list.update(True, x),
            lambda x: skip_list.update(False, x)]
    sops = [lambda x: str(x) in multiset, lambda x: multiset.add(str(x), x),
            lambda x: None if str(x) not in multiset else multiset.pop(str(x))]
    for op, c in argss:
        lres = lops[op](c)
        sres = sops[op](c)
        if op == 0:
            assert lres == sres
        assert skip_list.__len__() == multiset.__len__()


def test_light():
    common_test(2000, 4000)


def test_medium():
    common_test(4000, 10000)


def test_heavy():
    common_test(6000, 40000)
