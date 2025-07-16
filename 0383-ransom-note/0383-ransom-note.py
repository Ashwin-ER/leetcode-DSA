from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d = defaultdict(int)
        for char in magazine:
            d[char] += 1
        for char in ransomNote:
            if char not in d or d[char] <=0:
                return False
            d[char] -=1
        return True
         
        




        """count_ransom = {}
        count_mag = {}

        for i in ransomNote:
            if i in count_ransom:
                count_ransom[i] +=1
            else:
                count_ransom[i] =1

        for j in magazine:
            if j in count_mag:
                count_mag[i] +=1
            else:
                count_mag[i] =1
        
        for char in count_ransom:
            if count_ransom[char] > count_mag.get(char, 0):
                return False  

        return False
"""
            