class Solution:

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image = [x[::-1] for x in image]
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j] ^= 1

        return image