import * as deepDiff from "deep-diff";

const obj1 = {
  a: 5,
  v: 6,
  z: [1, 2, 4, [2, 5, 7]],
};
const obj2 = {
  a: 5,
  v: 7,
  z: [1, 2, 3, [1]],
};
const differences = deepDiff.diff(obj1, obj2);
console.log(differences);

function objDiff(obj1, obj2) {
  if (obj1 === obj2) {
    return {};
  }

  if (obj1 === null || obj2 === null) {
    return [obj1, obj2];
  }

  if (typeof obj1 !== "object" || typeof obj2 !== "object") {
    return [obj1, obj2];
  }

  if (Array.isArray(obj1) !== Array.isArray(obj2)) {
    return [obj1, obj2];
  }

  const result = {};
  for (const key in obj1) {
    if (key in obj2) {
      const diff = objDiff(obj1[key], obj2[key]);
      if (Object.keys(diff).length) {
        result[key] = diff;
      }
    }
  }

  return result;
}
