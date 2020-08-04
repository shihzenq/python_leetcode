import functools


class ClimbStairs:

    @functools.lru_cache(100)
    def climb_stairs(self, n: int) -> int:
        if n <= 2 : return  n
        return self.climb_stairs(n-1) + self.climb_stairs(n-2)


if __name__ == '__main__':
    c = ClimbStairs()
    res = c.climb_stairs(5)
    print(res)
