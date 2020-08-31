// 求两个数组的交集

function intersect(arr1: number[], arr2: number[]): number[] {
    let result: number[] = []
    // 1. 遍历长度最大的数组
    const len1 = arr1.length
    const len2 = arr2.length
    if (len1 < len2) {
        intersect(arr2, arr1)
    }
    // 2. 将数组中出现的元素和出现的次数保存到map中
    let map: Map<number, number> = new Map()
    for (let i = 0; i < len1; i++) {
        const count: number = (map.get(arr1[i]) || 0) + 1
        map.set(arr1[i], count)
    }
    // 3. 遍历第二个数组中的元素和map中存储的元素进行对比，如果有则存入result并将count减1
    for (let i = 0; i < len2; i++) {
        const count: number = map.get(arr2[i]) || 0
        if (count > 0) {
            result.push(arr2[i])
            map.set(arr2[i], count - 1)
        }
    }
    return result
}