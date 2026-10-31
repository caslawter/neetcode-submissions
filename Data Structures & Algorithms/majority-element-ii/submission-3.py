class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1 = None
        element2 = None
        count1 = 0
        count2 = 0
        ans = []

        for num in nums:
            if element1 == num:
                count1+= 1
            elif element2 == num:
                count2+= 1
            elif count1 == 0:
                element1 = num
                count1 += 1
            elif count2 == 0:
                element2 = num
                count2 += 1
            elif element1 != num and element2 != num:
                count1-=1
                count2-=1
            # print("element", element1, element2)
            # print("count", count1, count2)

        count1 = 0
        count2 = 0

        
        for num in nums:
            if num == element1:
                count1 += 1
            elif num == element2:
                count2 += 1

            
            if count1 > len(nums) // 3 and element1 not in ans:
                ans.append(element1)
            elif count2 > len(nums) // 3 and element2 not in ans:
                ans.append(element2)
        return ans
        