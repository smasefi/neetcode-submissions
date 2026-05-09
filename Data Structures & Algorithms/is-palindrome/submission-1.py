class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalnum():
                new_str += i
    
        new_str = new_str.lower()
        reversed_str = "".join(reversed(new_str))
        if new_str == reversed_str:
            return True

        else:
            return False
        
      