class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */

    getMap() {
    return new Map(
        Array.from({ length: 26 }, (_, i) => [String.fromCharCode(97 + i), 0]),
    );
}

    groupAnagrams(strs) {
    let ans = new Map();
    let result = [];
    for (let index = 0; index < strs.length; index++) {
        const element = strs[index];
        let frequencyMap = this.getMap();
        for (let index = 0; index < element.length; index++) {
            const char = element[index];
            let count = frequencyMap.get(char);
            frequencyMap.set(char, count + 1);
        }
        let string = JSON.stringify(Object.fromEntries(frequencyMap));
        if(ans.has(string)) {
            let temp = ans.get(string);
            temp.push(element);
            ans.set(string, temp)
        } else {
            ans.set(string, [element])
        }
    }
    ans.forEach((value,key) => {
        result.push(value);
    }); 
    
    return result;


    }
}
