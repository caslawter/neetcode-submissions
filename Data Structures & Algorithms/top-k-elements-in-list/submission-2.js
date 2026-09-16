class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
            let map = new Map();
    for (let index = 0; index < nums.length; index++) {
        const element = nums[index];
        if (map.has(element)) {
            map.set(element, map.get(element) + 1);
        } else {
            map.set(element, 1);
        }
    }
    let arr = new Array(map.size - 1);
    console.log(map);

    map.forEach((value, key) => {
        console.log(key);
        if (arr[value] == undefined) {
            let tempArr = [key];
            arr[value] = tempArr;
        } else {
            let tempArr = arr[value];
            tempArr.push(key);
            arr[value] = tempArr;
        }
    });
    arr = arr.flat()
    let counter = 0;
    let ans =[];
    
    for (let index = arr.length - 1; index >= 0; index--) {
        const element = arr[index];
        if(counter == k) break;
        counter++;
        ans.push(element)
    }    
    return ans;
    }
}
