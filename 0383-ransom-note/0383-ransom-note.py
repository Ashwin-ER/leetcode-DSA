class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine = list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            else:
                magazine.remove(ransomNote[i])
        return True


        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        """arr = []
        for i in range(len(ransomNote)):
            if i not in list(magazine):
                return False
            else:
                arr.append(i)
                ransomNote[i].pop()
                magazine[i].pop()
                if len(ransomNote)==0:
                    return True"""