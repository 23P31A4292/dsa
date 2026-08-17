class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        
        freq = Counter(s)
        freq2=Counter(t)
        if freq==freq2:
            return True
        return False

        
        
          