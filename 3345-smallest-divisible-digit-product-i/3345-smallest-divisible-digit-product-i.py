class Solution:
    def digitProduct(self, num: int) -> int:
        product = 1
        while num > 0:
            product *= num % 10
            num //= 10
        return product

    def smallestNumber(self, n: int, t: int) -> int:
        num = n
        while True:
            if self.digitProduct(num) % t == 0:
                return num
            num += 1