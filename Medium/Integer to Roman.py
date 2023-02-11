class Solution:
    def intToRoman(self, num: int) -> str:
        u = ""
        s1 = num // 1000
        if s1 != 0:
            num -= 1000 * s1
            u += "M" * s1
        s2 = num // 500
        if s2 != 0:
            num -= 500 * s2
            u += "D" * s2
        s3 = num // 100
        if s3 != 0:
            num -= 100 * s3
            u += "C" * s3
        s4 = num // 50
        if s4 != 0:
            num -= 50 * s4
            u += "L" * s4
        s5 = num // 10
        if s5 != 0:
            num -= 10 * s5
            u += "X" * s5
        s6 = num // 5
        if s6 != 0:
            num -= 5 * s6
            u += "V" * s6
        s7 = num // 1
        if s7 != 0:
            num -= 1 * s7
            u += "I" * s7
        u = u.replace("VIIII", "IX").replace("IIII", "IV")
        u = u.replace("LXXXX", "XC", ).replace("XXXX", "XL")
        u = u.replace("DCCCC", "CM", ).replace('CCCC', 'CD')
        return u
