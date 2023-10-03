from collections import defaultdict

class Solution:
    def countPairs(self, coordinates, k):
        m1 = defaultdict(int)
        ans = 0
        for i in range(len(coordinates)):
            for j in range(k + 1):
                a = coordinates[i][0] ^ j
                b = coordinates[i][1] ^ (k - j)
                if (a, b) in m1:
                    ans += m1[(a, b)]
            m1[(coordinates[i][0], coordinates[i][1])] += 1
        return ans
