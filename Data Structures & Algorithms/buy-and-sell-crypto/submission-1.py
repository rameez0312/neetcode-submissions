class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProf = 0
        
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[i]>prices[j]:
        #             continue
                
        #         prof = prices[j]- prices[i]
        #         maxProf = max(prof, maxProf)
        # return maxProf

        maxP=0
        l,r = 0,1

        while r<len(prices):
            if prices[r] > prices[l]:
                profit = prices[r]-prices[l]
                maxP = max(maxP,profit)
            else:
                l= r
            r +=1
        return maxP