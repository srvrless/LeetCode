

// JavaScript
Function.prototype.callPolyfill = function (context, ...args) {
  return this.call(context, ...args);
};


// TypeScript
declare global { 
    interface Function {
      callPolyfill(context: Record<any, any>, ...args: any[]): any;
	}
}

Function.prototype.callPolyfill = function(context, ...args): any {
    return this.call(context,...args)
}
