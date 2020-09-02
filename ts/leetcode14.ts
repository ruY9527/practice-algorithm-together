// leetcode13 最长公共前缀
// 编写一个函数来查找字符串数组中的最长公共前缀。
// 如果不存在公共前缀，返回空字符串 ""
/* 
    输入: ["flower","flow","flight"]
    输出: "fl"
*/

// 思路： 先拿到数据的第一个字符串赋值给result，然后遍历后面的字符与第一字符串逐一比较，如果发现不同直接跳出循环并在当前循环位置截取result

function longestCommonPrefix(strs: string[]): string {
    if (strs.length === 0) return ''
    if (strs.length === 1) return strs[0]

    let result = strs[0]
    for (let i = 1, len = strs.length; i < len; i++) {
        let j = 0
        for (; j < result.length && j < strs[i].length; j++) {
            if (result[j] !== strs[i][j]) {
                break
            }
        }
        result = result.substring(0, j)
        if (result === '') return ''
    }
    return result
}

console.log(longestCommonPrefix(["flower","flow","flight"]))