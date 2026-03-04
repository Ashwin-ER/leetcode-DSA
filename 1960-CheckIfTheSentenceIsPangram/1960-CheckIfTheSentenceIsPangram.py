# Last updated: 04/03/2026, 13:34:30
class Solution(object):
    def checkIfPangram(self, sentence):
        a = set(sentence)
        if len(a)==26:
            return True
        else:
            return False