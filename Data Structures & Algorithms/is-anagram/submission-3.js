class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
 let m = {};
    let g = {};

    for (let i = 0; i <= s.length - 1; i++) {
        if (m[`${s[i]}`] == undefined) {
            m[`${s[i]}`] = 1;
        } else {
            m[`${s[i]}`] += 1;
        }
    }

    for (let i = 0; i <= t.length - 1; i++) {
        if (g[`${t[i]}`] == undefined) {
            g[`${t[i]}`] = 1;
        } else {
            g[`${t[i]}`] += 1;
        }
    }

    
    if(Object.keys(g).length != Object.keys(m).length) return false;

    for (const key in m) {
        if (!Object.hasOwn(g, key)) return false;

        if(m[key] != g[key]){
            return false;
        }
        
    }
    return true;
    }
}
