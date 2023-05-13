const once = function (fn) {
    let val = false
    return function (...args) {
        if (!val) {
            val = true
            return fn(...args)
        }
    }
};