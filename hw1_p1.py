import random
import matplotlib.pyplot as plt
from typing import Tuple

def flipv1() -> str:
    return 'H' if random.randint(0, 1) else 'T'

def flipv2() -> str:
    if random.randint(0, 1) == 0:
        return 'T'
    else:
        return 'H'

def flipv3() -> str:
    if random.random() < 0.5:
        return 'T'
    else:
        return 'H'

def flipperv1(n: int) -> Tuple[int, int]:
    res = [flipv1() for _ in range(n)]
    return res.count('H'), res.count('T')

def flipperv2(n: int) -> Tuple[int, int]:
    heads = 0
    tails = 0
    for _ in range(n):
        if flipv1() == 'H':
            heads += 1
        else:
            tails += 1

    return heads, tails

plt.bar(['H', 'T'], flipperv1(1000))
plt.show()

plt.bar(['H', 'T'], flipperv2(500))
plt.show()


def unfair_flip(p_head: float = 0.3) -> str:
    if random.random() <= p_head:
        return 'H'
    else:
        return 'T'

def unfair_flipper(n: int, p_head: float = 0.3) -> Tuple[int, int]:
    res = [unfair_flip(p_head) for _ in range(n)]
    return res.count('H'), res.count('T')

plt.bar(['H', 'T'], unfair_flipper(1000))
plt.show()
plt.bar(['H', 'T'], unfair_flipper(1000, p_head=0.1))
plt.show()

def plot_flips(n: int, p_head: float = 0.3) -> None:
    plt.bar(['H', 'T'], unfair_flipper(n, p_head))
    plt.ylabel('Number of flips')
    plt.title(f'{n} coin flips with prob(head) = {p_head}')
    plt.show()

