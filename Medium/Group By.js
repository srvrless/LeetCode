// JavaScript
Array.prototype.groupBy = function(fn) {
  return _.groupBy(this, fn)
};
z

// TypeScript Version
declare global {
  interface Array<T> {
    groupBy(fn: (item: T) => string): Record<string, T[]>;
  }
}

Array.prototype.groupBy = function (fn) {
  return _.groupBy(this, fn);
};
