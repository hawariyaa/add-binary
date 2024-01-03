# here in this leet code we are asked to add to binary numbers given as string
# and we are going to return a string too
# ord in python gives us the asci value of the character example: ord(a)  = 97
# here we did ord(a[i]) - ord("0") know this will give us if a[i] = 1, it will give us the interger 1
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a[::-1], b[::-1]
        sum = ""
        carry = 0
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0
            total = digitA + digitB + carry
            char = str(total % 2)
            sum = char + sum  # here is we put the char to the biggining of the sum
            carry = total // 2
        if carry:
            sum = "1" + sum # here also we want to add 1 to the biggingig of the sum

        return sum