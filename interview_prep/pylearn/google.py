class Solution:

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        pass

    def licenseKeyFormattingII(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        len_S = len(S)

        keys = []

        if len_S % K != 0:
            first = slice(0, len_S % K)
            k = len_S % K
        else:
            first = slice(0, K)
            k = K

        keys.append(S[first])

        for i in range(1, n_iter + 1):
            mid = slice(i * K - k, (i + 1) * K - k)
            keys.append(''.join(S[mid]))
            #print("{}: {}".format(i, keys[i]))

        return '-'.join(keys)

    def licenseKeyFormatting(self, S, K):
        keys = []
        S = S.upper().replace("-", "")
        step_size = K
        n_steps = len(S) // K

        for i in range(0, n_steps):
            slice_dad = slice(i * step_size, (i + 1) * step_size)
            keys.append(S[slice_dad])
            # print("slice: {}".format(slice_dad))
            # print("{}".format(S[slice_dad]))

        return '-'.join(keys)


if __name__ == '__main__':
    s = Solution()
    print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
    print(s.licenseKeyFormatting("2-5g-3-J", 2))
