from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        cnt = Counter(s)

        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i

        return -1