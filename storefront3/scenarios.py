# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements 
# in nums which are not equal to val be k, 
# to get accepted, you need to do the following things:
# Change the array nums such that the first 
# k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k

# solution:

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
            return index

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]
# Explanation: The current max value is 5 which is held by Kid 3

# Kid 1, they will have 2 + 3 = 5 candies, which is greater or equal to the current max of 5.
# Kid 2, they will have 3 + 3 = 6 candies, which is greater or equal to the current max of 5.
# Kid 3, they will have 5 + 3 = 8 candies, which is greater or equal to the current max of 5.
# Kid 4, they will have 1 + 3 = 4 candies, which is less than the current max of 5.
# Kid 5, they will have 3 + 3 = 6 candies, which is greater or equal to the current max of 5.

class PreSolution2:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
# changed candies to c and then extraCandies to eC in def

class Solution2:
    def kidsWithCandies(self, c: List[int], eC: int) -> List[bool]:
        return [x+eC >= max(c)for x in c]
    
#  Reverse Vowels of a String
#  input = hello
# desired output = holle

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s) # convert string to list
        vowels = set("aeiouAEIOU")
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] not in vowels:
                low += 1
            elif s[high] not in vowels:
                high -= 1
            else:
                s[low], s[high] = s[high], s[low] # swap the chars
                low += 1
                high -= 1
        return "".join(s) # convert list to string
    

# Find the Highest Altitude
# given an integer array gain of length n where gain[i] 
# is the net gain in altitude between points i​​​​​​ and i + 1

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = 0
        maxVal = 0
        for i in gain:
            a+=i
            maxVal=max(a,maxVal)
        return maxVal
