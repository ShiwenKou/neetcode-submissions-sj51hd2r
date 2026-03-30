class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # we need to have a hash map for order, so that we can compare  ✅


        # focus on a window of two words, if violates condition return false. ✅


        # substring

        from collections import defaultdict
        hash_map = {}

        for index, char in enumerate(order):
            hash_map[char] = index
        

        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i + 1]

            
            for j in range(min(len(first_word), len(second_word))):

                char_1 = first_word[j]
                char_2 = second_word[j]

                if char_1 != char_2:
                
                    if hash_map[char_1] > hash_map[char_2]:
                        return False # inconsistency find
                    break
            
            else:
                if len(first_word) > len(second_word):
                    return False
        return True
                


        