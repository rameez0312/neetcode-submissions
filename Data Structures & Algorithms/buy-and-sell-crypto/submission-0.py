class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i]>prices[j]:
                    continue
                
                prof = prices[j]- prices[i]
                maxProf = max(prof, maxProf)
        return maxProf