// leetcode 20 (有效的括号)

function isValid(str: string) {
    const length: number = str.length
    if (length % 2 === 1) return false
    const obj = {
        '{':'}',
        '[':']',
        '(':')'
    }
    let stack: Array<string> = []
    for (let i = 0, len = length; i < len; i++) {
        const s: string = str[i]
        if (obj[s]) {
            stack.push(obj[s])
        } else {
            if (s !== stack[stack.length-1]) return false
            stack.pop()
        }
    }
    return stack.length === 0
}

console.log(isValid('{}'))
console.log(isValid('([])}'))