import math
def threeSum(nums):
        result = []
        nums.sort()
        l = len(nums)
        maxComb = math.factorial(l)/(6*math.factorial(l-3))
        p1 = 0 # 0, len(nums)-2 - 4
        p2 = 1 # Rand 1, len(nums) - 5
        p3 = 2 # Range 2, len(nums)-2 - 4
        sum = 0
        #x + y + z = 0
        counter = 0
        potentialCombinations = [
        [nums[0] , nums[1] , nums[2]],
        [nums[0] , nums[1] , nums[3]],
        [nums[0] , nums[1] , nums[4]],
        [nums[0] , nums[1] , nums[5]],

        [nums[0] , nums[2] , nums[3]],
        [nums[0] , nums[2] , nums[4]],
        [nums[0] , nums[2] , nums[5]],
        
        [nums[0] , nums[3] , nums[4]],
        [nums[0] , nums[3] , nums[5]],
        [nums[0] , nums[4] , nums[5]],
        
        [nums[1] , nums[2] , nums[3]],
        [nums[1] , nums[2] , nums[4]],
        [nums[1] , nums[2] , nums[5]],

        [nums[1] , nums[3] , nums[4]],
        [nums[1] , nums[3] , nums[5]],

        [nums[1] , nums[4] , nums[5]],
        
        [nums[2] , nums[3] , nums[4]],
        [nums[2] , nums[3] , nums[5]],
        [nums[2] , nums[4] , nums[5]],

        [nums[3] , nums[4] , nums[5]]
        ]

        for list in potentialCombinations:
            counter += 1
            for n in list:
                sum += n
            if sum == 0:
                if list in result:
                    pass
                else:
                    result.append(list)
            print(counter)
            print(list)
            print(sum)
            print(result)
            sum = 0
        # for r in result:
        #     if r[0] and r[1] and r[2] in :
        #         pass
        #     else:

        # for n in nums:
        #     n1 = nums[p1]
        #     n2 = nums[l+p2]
        #     x = n1 + n2
        #     print(x)
        #     if x in nums[p1+1:p2]:
        #         print("YES")
        #         result.append([n1, n2, x])
        #         p1 += 1
        #     elif x < 0 and abs(n1) > n2:
        #          p1+=1
        #     else:
        #          p2-=1

        #     print(nums[p1+1:p2]) 
            
        
        

        return result

#nums = [-1,0,1,2,-1,-4]
#nums = [-4,-1,-1,0,1,2]
nums = [0,1,1]


print(threeSum(nums))