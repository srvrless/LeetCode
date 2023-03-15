class Solution:

    def licenseKeyFormatting(self, s, k):

        S = s.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i + k] for i in range(0, len(S), k))[::-1]
