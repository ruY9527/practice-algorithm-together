// leetcode 20 (有效的括号)

function isValid(str) {
    const length = str.length
    if (length % 2 === 1) {
        return false
    }
    const obj = {
        '{':'}',
        '[':']',
        '(':')'
    }
    let stack = []
    for (let i = 0, len = length; i < len;i++) {
        const s = str[i]
        if (obj[s]) {
            stack.push(obj[s])
        } else {   
            if (s !== stack[stack.length-1]) {
                return false
            } else {
                stack.pop()
            }
        }
    }
    return stack.length === 0
}

console.log(isValid('}'));