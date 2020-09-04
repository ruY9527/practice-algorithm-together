let vs = [0,2,4,3,7] // 物品的价值
let ws = [0,2,3,5,5] // 物品的重量

function ks(i: number, j: number): string {
    // 默认什么都没有装
    let results = []
    for (let m = 0; m <= i; m++) {
        results[m] = []
        results[m][0] = 0
    }
    for (let m = 0; m <= j; m++) {
        results[0][m] = 0
    }
    for (let m = 1; m <= i; m++) {
        for (let n = 1; n <= j; n++ ) { // n 背包可以承受的重量
            if (n < ws[m]) { // 装不下去
                results[m][n] = results[m - 1][n]
            } else {
                // 不装）
                if (results[m - 1][n] > results[m - 1][n - ws[m]] + vs[m]) {
                    results[m][n] = results[m - 1][n]
                } else {
                    // 装
                    results[m][n] = results[m - 1][n - ws[m]] + vs[m]  
                }
            }
        }
    }
    // 找到被选中的物品
    let m = i
    let n = j
    let k = []
    while (m > 0) {
        if (results[m][n] !== results[m - 1][n]) {
            n -= ws[m]
            k.push(m)
        }
        m--
    }
    let result = `当你装下第${k.join('、')}个物品时，能达到收益最大，收益为${results[i][j]}`
    return result
}
console.log(ks(4, 10)); // 背包可承受10的重量，4个物品