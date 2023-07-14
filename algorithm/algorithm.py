# pylint: disable=C0116
from functools import reduce
from operator import add

# Q001: haskell の zip と同様の機能の関数 my_zip を書け （パラメータの数は可変であること）
# zip :: [a] -> [b] -> [(a, b)]


def my_zip(*xs):
    if not xs:
        return None
    return list(map(lambda *x: tuple(x), *xs))

# Q002: haskell の sum と同様の機能の関数 my_sum を書け。
# sum :: (Num a) => [a] -> a
# sum ns
#     数値のリスト ns の総和を返す。
#     see also: product, foldl
#         sum [1, 2, 3]  = 6
#         sum []         = 0


def my_sum(ns):
    if not ns:
        return 0
    return reduce(add, ns)

# Q003: クイックソート関数 qsort01 を書け（リスト内包表記を使うこと）


def qsort01(xs):
    if not xs:
        return []
    x, *rest = xs
    lt = [_x for _x in rest if _x < x]
    ge = [_x for _x in rest if _x >= x]
    return sum([qsort01(lt), [x], qsort01(ge)], [])
