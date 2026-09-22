class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        numbers= {}
        counter= 0
        for num in nums:
            if num not in numbers and num > 0: 
                numbers[num]= True
                counter+= 1

        for i in range(1, counter+1):
            if i not in numbers:
                return i
        return counter+1
            