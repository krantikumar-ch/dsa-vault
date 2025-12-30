3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Approach

Solved using sliding window technique + HashMap data structure

core idea is traverse from left to end
store key and index
calculate distance from right to left i.e., right - left + 1
if it is max update it
in middle check that is present in dict if yes update start
make two pointers left and right at 0th index
create index dictionary holding character is key value is index
