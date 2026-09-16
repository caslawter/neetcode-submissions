class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
    let map = new Map();

    for (let i = 0; i <= nums.length - 1; i++) {
        map.set(nums[i], i);
    }

    for (let i = 0; i <= nums.length - 1; i++) {
        let complement = target - nums[i];
        let position = map.get(complement);
        if(position != undefined && position != i) return [i, position];
        else continue;
    }

    }
}
