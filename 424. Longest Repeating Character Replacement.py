# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        s_list = list(s)
        count_map ={}
        
        
        for right in range(len(s_list)):

            count_map[s_list[right]] = count_map.get(s_list[right], 0) + 1

            max_key = max ( count_map , key = count_map.get)
            window_size = right - left + 1

            if window_size - count_map[max_key] > k :
                
                count_map[s_list[left]] = count_map.get(s_list[left]) - 1
                left += 1
                window_size = right - left + 1

        return window_size  
