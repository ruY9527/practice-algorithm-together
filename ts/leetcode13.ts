// leetcode 13 罗马数字转整数

function romanToInt(s: string): number {
    const obj = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000 
    }
    const lastIndex: number = s.length - 1
    let result: number = obj[s[lastIndex]] // 默认赋值最后一位的字符所代表的数字
    for (let i = lastIndex; i > 0; i--) { // 1. 从右向左遍历字符串
        const curNum: number = obj[s[i]]
        const frontNum: number = obj[s[i - 1]]
        if (curNum === frontNum || curNum < frontNum) { // 2. 如果右边的字符代表的数字比自己代表的数字大则相加反之相减
            result += frontNum
        } else {
            result -= frontNum
        }
    }
    return result
}

romanToInt('CIV')