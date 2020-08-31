// 最长上升子序列的上升长度


function lengthOfLIS(arr: number[]): number {
    const len = arr.length
    if (len <= 1) return len
    let dp = arr.map(() => 1)
    for (let i = 1; i < len; i++) {
        let j = i - 1
        while (j >= 0) {
            if (arr[i] > arr[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1) // 比前面的元素大则在前一个元素的lts长度上加1
            }
            j--
        }
    }
    return Math.max(...dp)
}

console.log(lengthOfLIS([10,9,2,5,3,7,101,18]))