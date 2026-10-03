class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # Agar duplicate current window me hai, left pointer jump karega
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            
            # Character ka latest index save karo
            last_seen[char] = right
            
            # Max window size calculate karo
            max_len = max(max_len, right - left + 1)
            
        return max_len