"""
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output
will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary
representation is the same, whether it is signed or unsigned. In Java, the compiler represents the signed integers
using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the
output represents the signed integer -1073741825.


Example 1:

Input: n = 00000010100101000001111010011100 Output:    964176192 (00111001011110000010100101000000) Explanation: The
input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192
which its binary representation is 00111001011110000010100101000000. Example 2:

Input: n = 11111111111111111111111111111101 Output:   3221225471 (10111111111111111111111111111111) Explanation: The
input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471
which its binary representation is 10111111111111111111111111111111. """


class Solution:
    # Inefficient Solution: Since we are converting to string, filling, converting back to int and multiplying.
    def reverseBits1(self, n: int) -> int:
        bin_format = format(n, 'b').zfill(32)
        revnum = 0
        for i in range(len(bin_format)):
            revnum += int(bin_format[i]) * (2 ** i)

        return revnum

    # Optimal bitwise solution
    # Left shift by one and add the last bit of the current number (Get by &). Keep repeating for 32 bits.
    def reverseBits2(self, n: int) -> int:
        res = 0

        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1

        return res


testcases = [43261596,
             4294967293]

sol = Solution()

for testcase in testcases:
    print('Input:', testcase,
          '\nOutput 1:', sol.reverseBits1(testcase),
          '\nOutput 2:', sol.reverseBits2(testcase), '\n')
