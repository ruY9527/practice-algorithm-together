/* 
* 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
* 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
* 链接：https://leetcode-cn.com/problems/two-sum
*/

// 示例
/* 
* 给定 nums = [2, 7, 11, 15], target = 9
* 因为 nums[0] + nums[1] = 2 + 7 = 9
* 所以返回 [0, 1] 
*/

function twoSum(nums, target){
    let map = new Map()
    for (let i = 0, len = nums.length; i < len; i++) {
        let diff = target - nums[i]
        if (map.has(diff)) {
            let index = map.get(diff)
            return [index, i]
        } else {
            map.set(nums[i], i)
        }
    }
    return [0, 0]
}
console.log(twoSum([2, 7, 11, 15], 9))