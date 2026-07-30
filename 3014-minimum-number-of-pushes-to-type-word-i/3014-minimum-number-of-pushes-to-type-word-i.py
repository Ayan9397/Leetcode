class Solution:
    def minimumPushes(self, word: str) -> int:
        length = len(word)
        total_pushes = 0
        
        # Iterate through each character in the word
        for i in range(length):
            # i // 8 calculates how many sets of 8 keys have been fully mapped
            # Adding 1 gives the current push cost for the character
            total_pushes += (i // 8) + 1
            
        return total_pushes