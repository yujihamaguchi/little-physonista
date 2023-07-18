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

# Q004: Haskell の product と同様の機能の関数を書け(再帰を用いるパターン、 reduce を用いるパターン、 apply を用いるパターン)
# product :: (Num a) => [a] -> a
# product ns
#     数値のリスト ns の全要素の積を返す。
#         product [2, 3, 4]   = 24
#         product [4, 5, 0]   = 0
#         product []          = 1


def product(ns):
    return reduce(lambda acc, n: acc * n, ns, 1)


# Q007: Haskell の last と同様の機能の関数 my_last を書け
# last :: [a] -> a
#     リストの最後の要素を返す。
#         last [1,2,3]   = 3
#         last []        = エラー
def my_last(xs):
    if not xs:
        raise ValueError()
    return list(reversed(xs))[0]


# Q008: 偶数の長さを持つリストを半分ずつに分割する関数 halve を書け。
def halve(xs):
    length = len(xs)
    if length == 0 or length % 2 != 0:
        raise ValueError()
    n = length // 2
    return (xs[:n], xs[n:])

