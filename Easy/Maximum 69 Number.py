class Solution:
    def maximum69Number (self, num: int) -> int:
        num_lst = list(str(num))
        if '6' in num_lst:
            num_index = num_lst.index('6')
            num_lst[num_index] = '9'
            return int(''.join(num_lst))
        else:
            return num