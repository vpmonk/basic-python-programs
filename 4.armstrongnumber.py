class Solution:
    def armstrongNumber (self, n):
        og_n=n
        result = 0
        while n!=0:
            arm = n%10
            result = arm**3+result
            n=n//10
            
        if og_n==result:
           return "Yes" 
        else:
           return "No"
