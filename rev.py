# n = 245
# x = 121
# rev =0
# while(n!=0):
#     nu = n%10
#     rev = rev*10+nu
#     n=n//10



# print(rev)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        rev =0
        while(n!=0):
            nu = n%10
            rev = rev*10+nu
            n=n//10
            
        if(x == rev):
            return True
        else:
            return False
        