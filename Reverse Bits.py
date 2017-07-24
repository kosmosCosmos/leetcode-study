class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(4):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

    def reverseBits2(self, n):
        string = bin(n)
        if '-' in string:
            string = string[:3] + string[3:].zfill(4)[::-1]
        else:
            string = string[:2] + string[2:].zfill(4)[::-1]
        return int(string, 2)

if __name__ == '__main__':
    for i in  range(1000):
        Solution().reverseBits2(i)
