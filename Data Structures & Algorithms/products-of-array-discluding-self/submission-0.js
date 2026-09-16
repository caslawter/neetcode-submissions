class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
            let prefix = new Array(nums.length);
    let suffix = new Array(nums.length);
    let ans = [];
    let prefixProduct = 1;
    for (let index = 0; index < nums.length; index++) {
        const element = nums[index];
        prefix[index] = prefixProduct;
        prefixProduct *= element;
    }
    console.log(prefix);

    let suffixProduct = 1;

    for (let index = nums.length - 1; index >= 0; index--) {
        const element = nums[index];
        suffix[index] = suffixProduct;
        suffixProduct *= element;
    }

    for (let index = 0; index < nums.length; index++) {
        ans.push(suffix[index] * prefix[index])
    }
    return ans;
    }
}
