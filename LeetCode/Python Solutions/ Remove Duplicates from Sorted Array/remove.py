from typing iomport List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> -> List[int]:
        print(list(set(nums)))


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.removeDuplicates([1,1,2])  #  [1,1,2] -> [1,2]
    print(Solve)