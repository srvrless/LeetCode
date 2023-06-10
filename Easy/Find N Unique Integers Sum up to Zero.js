var sumZero = function(n) {
    let arr = [];
    let sum = 0;
    for (let i = 1; i < n; i++) {
        arr.push(i);
        sum += i;
    }
    arr.push(-sum);
    return arr;
}

// Python3 Solution
// class Solution:
//     def sumZero(self, n: int) -> List[int]:
//         result = [0] * n
//         for i in range(n // 2):
//             result[i] = -(i + 1)
//             result[n - i - 1] = i + 1
//         return result
