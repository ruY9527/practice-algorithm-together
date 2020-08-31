package com..service.test;

import com.JsonUtils;
import org.junit.Test;

/**
 * @author ：wangsun
 * @date ：Created in 2020/8/28 16:18
 * @project : user
 * @package : com.service.test
 * @description：测试
 */
public class Solution {

    /**
     * @Author :
     * @Date : 2020/8/28
     * @Param :a
     * @Return :
     * @Description : 给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
     *                并返回他们的数组下标。
     */
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length-1; j++) {
                if (nums[i]+nums[j]==target){
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
        return null;
    }

    @Test
        public void testTwoSum(){
        int[] nums = {3, 2, 4, 15};
        int target = 6;

        int[] ints = twoSum(nums, target);

        System.out.println("ints is "+ JsonUtils.deserializer(ints));
    }
}
