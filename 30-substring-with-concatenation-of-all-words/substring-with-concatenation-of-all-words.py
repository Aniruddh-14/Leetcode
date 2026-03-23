class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        from collections import Counter
        word_map = Counter(words)

        result = []

        # Try all starting offsets
        for i in range(word_len):
            left = i
            count = 0
            seen = {}

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_map:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    # If extra occurrence → shrink window
                    while seen[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # Valid window found
                    if count == total_words:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    # Reset window
                    seen.clear()
                    count = 0
                    left = j + word_len

        return result