

// TypeScript Solutinon
type F = () => Promise<any>;

async function promisePool(functions: F[], n: number): Promise<any[]> {
    const results: any[] = [];
    const inProgress: Promise<any>[] = [];
    let i = 0;

    while (i < functions.length || inProgress.length > 0) {
        while (inProgress.length < n && i < functions.length) {
            const promise = functions[i]();
            const index = i;
            const resultPromise = promise.then((result) => {
                results[index] = result;
                inProgress.splice(inProgress.indexOf(resultPromise), 1);
            });
            inProgress.push(resultPromise);
            i++;
        }

        await Promise.race(inProgress);
    }
    return results;
}

// JavaScript Solution
const promisePool = async function (functions, n) {
    const results = []
    const inProgress = []
    let i = 0
    while (i < functions.length || inProgress.length > 0) {
        while (inProgress.length < n && i < functions.length) {
            const promise = functions[i]();
            const index = i;
            const resultPromise = promise.then((result) => {
                results[index] = result;
                inProgress.splice(inProgress.indexOf(resultPromise), 1);
            });
            inProgress.push(resultPromise);
            i++;
        }

        await Promise.race(inProgress);
    }

    return results;
};