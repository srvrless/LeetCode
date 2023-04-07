class Solution:

    def squareIsWhite(self, coordinates: str) -> bool:
        disck = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8
        }
        my_list = [[False, True, False, True, False, True, False, True],
                   [True, False, True, False, True, False, True, False],
                   [False, True, False, True, False, True, False, True],
                   [True, False, True, False, True, False, True, False],
                   [False, True, False, True, False, True, False, True],
                   [True, False, True, False, True, False, True, False],
                   [False, True, False, True, False, True, False, True],
                   [True, False, True, False, True, False, True, False]]

        row = int(coordinates[1]) - 1
        col = disck.get(coordinates[0]) - 1

        return my_list[row][col]  