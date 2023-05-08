const map = function (arr, fn) {
    let count = 0
    return arr.map(x => fn(x, count++))
}

const map1 = function (arr, fn) {
    const newArr = new Array(arr.length);
    for (let i = 0; i < arr.length; i++) {
        newArr[i] = fn(arr[i], i);
    };

    return newArr;
};