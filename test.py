# %%
import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
nx, ny = 50, 50  # 格子点数（x, y方向）
dx, dy = 1.0, 1.0  # 格子間隔
D = 1.0  # 拡散係数
dt = 0.1  # タイムステップ
nsteps = 100  # シミュレーションのステップ数（画像の枚数）

# 初期条件：中央に局所的なピークを与える
u = np.zeros((nx, ny))  # (a, b)はタプルで...

u[nx // 3 : nx * 2 // 3, ny // 3 : ny * 2 // 3] = 100.0


def update(u, dt, dx, dy, D):
    """
    uの内部点に対して中心差分でラプラシアンを計算し、
    拡散方程式に従って次の状態を返す。
    """
    u_new = u.copy()
    # 内部点の更新（境界は固定）
    u_new[1:-1, 1:-1] = u[1:-1, 1:-1] + D * dt * (
        (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[0:-2, 1:-1]) / dx**2
        + (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, 0:-2]) / dy**2
    )
    return u_new


# シミュレーションと画像保存
for i in range(nsteps):
    plt.figure(figsize=(5, 4))
    im = plt.imshow(u, cmap="hot", origin="lower", vmin=0, vmax=100)
    plt.title(f"2D Diffusion Equation, Step {i}")
    plt.colorbar(im)
    # 画像をファイルに保存（例：diffusion_000.png, diffusion_001.png, ...）
    plt.show()
    # plt.savefig(f"diffusion_{i:03d}.png")
    # plt.close()

    # 次の状態へ更新
    u = update(u, dt, dx, dy, D)
