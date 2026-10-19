class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window_length
        # replacements
        # k

        # replacements = window_length - most_repeating_char

        # replacements == k:
        # valid window

        # replacements < k:
        # valid window

        # replacements > k:
        # move both pointers of the window so that it becomes valid

        left = 0
        right = 1
        best_len = 1
        most_freq_element = {}
        most_freq_element[s[left]] = 1

        while right < len(s):
            print("left", left)
            print("right", right)
            print("s left", s[left])
            print("s right", s[right])
            if s[right] in most_freq_element:
                most_freq_element[s[right]] += 1
            else:
                most_freq_element[s[right]] = 1

            window_length = (right - left) + 1
            print("most_freq_element", most_freq_element)
            print("most freq",  max(most_freq_element.values()))
            replacements = window_length - max(most_freq_element.values())
            print("replacements", replacements)
            if replacements == k or replacements < k:
                best_len = window_length
                right += 1
            else:
                most_freq_element[s[left]] -= 1
                left += 1
                right += 1


        return best_len



sol = Solution()
s = "AABABBA"
k = 1
print(sol.characterReplacement(s, k))
