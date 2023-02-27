class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            '10#': "j",
            '11#': "k",
            '12#': "l",
            '13#': "m",
            '14#': "n",
            '15#': "o",
            '16#': "p",
            '17#': "q",
            '18#': "r",
            '19#': "s",
            '20#': "t",
            '21#': "u",
            '22#': "v",
            '23#': "w",
            '24#': "x",
            '25#': "y",
            '26#': 'z'
        }

        new = ''
        while s:
            if s[:3] in dic:
                new += dic[s[:3]]
                s = s[3:]
                continue
            if s[0] in dic:
                new += dic[s[0]]
                s = s[1:]

        return new
