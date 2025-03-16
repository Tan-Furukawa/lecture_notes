# %%
import numpy as np

# 型-----------------------------

# 整数型
x1: int = 1
# 小数型
x2: float = 1.0
# bool型
x3: bool = False
# 文字型
x4: str = "hello goodbye"



# 二項演算子----------------------------
x = 2 * 5
y = 3

## (A, A) -> A型
z = x * y
print(z)
z = x - y
print(z)
z = x + y
print(z)


## (A, A) -> float型
z = x / y
print(z)

## (A, A) -> bool型
z = x == y
print(z)
