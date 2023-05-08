const createCounter = (init) => {
    let count = init;
  
    return {
      increment: () => {
        count++;
        return count;
      },
  
      decrement: () => {
        count--;
        return count;
      },
  
      reset: () => {
        count = init;
        return count;
      }
    };
  }
// var createCounter1 = function(init) {
//     let presentCount = init
//     return {
//         increment:()=> ++presentCount,
//         decrement:()=> --presentCount,
//         reset:()=> presentCount = init,
//     }
// };