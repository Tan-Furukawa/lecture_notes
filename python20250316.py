# %%
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
# %%


# 型-----------------------------
# :型の形で書く。書いても書かなくてもいい

# 整数型
x1: int = 1
# 小数型
x2: float = 1.0
# bool型
x3: bool = False
# 文字型
x4: str = "hello goodbye"
# None型 (応用、気にしなくていい)
x5: None = None
# NDArray型 (numpy array専用)
# np.linspace(start: float, end: float, 数: int)
x6: NDArray = np.linspace(0.0, 10.0, 100)
x7: NDArray = np.random.random(100)
x8: NDArray = np.zeros((100,))
x9: NDArray = np.ones((100,))

# これ以外にも無限にある

# %%

# 二項演算子----------------------------
# 整数や実数に対して
x = 2 * 5
y = 3

## (A, A) -> A型
print(x * y)
print(x - y)
print(x + y)

## (A, A) -> float型
print(x / y)

## (A, A) -> bool型
z = x == y
print(z)

## (bool, bool) -> bool型
# and 演算子（かつ)
print((x == y) and False)
# print( x*y and False) 意味不明だから使わない

## (bool, bool) -> bool型
# or 演算子 （または）
print((x == y) or False)

# %%
# 文字に対しても２項演算子が使えるときがある。
p: str = "hello"
q: str = "goodbye"
print(p + q)
print(p == q)
# print(p * 3) なるべくやらない
# print(p - q)  # error
# print(p / q)  # error

# %%
# １項演算子
# bool -> bool

s = False
print(not s)
# print(not 1)

# 組み合わせ

# %%
# トリッキーな演算子
# []演算子
# (Array of A, int) -> A
vec = np.linspace(0.0, 1.0, 100)
print(vec[10])


# %%

# 関数


def add(x: int, y: int) -> int:
    return x + y


# とりあえずは型は書かなくてもよい
def add2(x, y):
    return x + y

def add_double(x: int, y: int) -> int:
    return x + y * 2


print(add(add(1, 2), 3))

print(add_double(10, 11))

# %%
