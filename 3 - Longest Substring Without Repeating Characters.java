/*
Given a string s, find the length of the longest 
substring
without repeating characters.

 
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/


class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int max = 0;
        int cur = 0;
        char[] carr = s.toCharArray();
        for(int i=0; i!=carr.length; i++){
            Set<Character> l = new TreeSet();
            for(int j=i; j!=carr.length && !l.contains(carr[j]); j++){
                cur++;
                l.add(carr[j]);
            }
            max = Math.max(cur, max);
            cur=0;
        }
        return max;
    }
}
