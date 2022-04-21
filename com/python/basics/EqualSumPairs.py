from itertools import combinations

from SearchCommonElements import SearchCommonElements


class EqualSumPairs(SearchCommonElements):

    def combinations(iterable):
        """Return r=2 combinations of an iterable."""
        # Inherently, r=2 (pairs) by using two loops
        pool = []
        for idx_i, i in enumerate(iterable):
            for idx_j, j in enumerate(iterable):
                if (idx_i != idx_j) and ((j, i) not in pool):
                    pool.append((i, j))
        return pool

    def get_sums(iterable, target):
        """Return the tally of summed paired equal to the target value."""
        results = [sum(i) for i in combinations(lst)]
        return len([i for i in results if i == 5])

    get_sums([1, 4, 6, 7, 8], 5)