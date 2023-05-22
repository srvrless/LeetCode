// 1 million rps

function jsonStringify(object: any): string {
  return JSON.stringify(object);
}

// idk
function jsonStringify(object: any): string {
    if (typeof object === 'string') return `"${object}"`
    if (typeof object === 'number' || typeof object === 'boolean' || object === null) return `${object}`

    if (Array.isArray(object)) {
        return `[${object.map(jsonStringify).join(',')}]`
    }

    const propertyStrings = []

    for (let key in object) {
        propertyStrings.push(`"${key}":${jsonStringify(object[key])}`)
    }
 
    return `{${propertyStrings.join(',')}}`
};