class Solution(object):
    def mostWordsFound(self, sentences):
        """a = len(sentences)
        return a"""
        max_words = 0
        for s in sentences:
            words = s.count(" ") + 1
            if words > max_words:
                max_words = words
        return max_words

        
            


        