// leetcode6 Z字变换 （将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列）
// 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
// L   C   I   R
// E T O E S I I G
// E   D   H   N
// 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"

// 思路： 观察例子中的排列是的字符串 可以发现当我们把空格去掉后就是一个长度为3的数据，所以我们可以遍历原始字符串然后生成一个数组然后在将数组拼接起来

function convert(strs: string, numRows: number): string {
    if (numRows === 1 || strs.length <= numRows) return strs

    // 生成长度为numRows的空字符串数组数组
    let rows = []
    for (let i = 0; i < numRows; i++) {
        rows[i] = ''
    }

    let col = 0 // 数组的所以
    let down = false // 字符串是否在数组的下一个索引进行拼接

    for (const s of strs) {
        rows[col] += s
        if (col === 0 || col === numRows - 1) { // 在达到变换的边界时改变down值
            down = !down
        }
        col += down ? 1 : -1 // down为ture时举行在数组的下一个索引值上追加，为false时则在上一个所以值增加
    }

    return rows.join('')
}

console.log(convert('PAYPALISHIRING', 3));