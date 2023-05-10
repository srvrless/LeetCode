
const filter = function (arr, fn) {
    let res = [];
    arr.forEach((value, curr) => {
        if (fn(value, curr)) {
            res.push(value);
        }
    })
    return res;
};