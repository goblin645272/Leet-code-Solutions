class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = int(num**0.5)
        if root**2 == num:
            return True
