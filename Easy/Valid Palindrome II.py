def validPalindrome(self, s: str) -> bool:
	L = len(s)
	for i in range(L//2+1):
		if (s[i] != s[-i-1]):
			return s[i+1:L-i] == s[i+1:L-i][::-1] or s[i:L-i-1] == s[i:L-i-1][::-1]
	return True