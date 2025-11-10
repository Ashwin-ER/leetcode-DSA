class Solution(object):
    def checkIfPangram(self, sentence):
        a = set(sentence)
        if len(a)==26:
            return True
        else:
            return False