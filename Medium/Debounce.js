
// TypeScript
type F = (...p: any[]) => any

const debounce = (fn: F, t: number): F => {
    let timeout: ReturnType<typeof setTimeout>
    return (...args) => {
        clearTimeout(timeout)
        timeout = setTimeout(() => fn(...args), t)
    }
}


// JavaScript
const debounce = (fn, t) => {
    let timeoutId;
  
    return (...args) => {
      clearTimeout(timeoutId);
  
      timeoutId = setTimeout(() => {
        fn.apply(this, args);
      }, t);
    };
  };