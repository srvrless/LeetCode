def isPalindrome(s):
    s = ''.join([x for x in s if x.isdigit() or x.isalpha()])
    if s == s[::-1]:
        return True
    return False
