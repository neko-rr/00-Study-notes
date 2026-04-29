# 383. Ransom Note（leetcode）
- 特徴：個数関係する照合＝辞書型

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

```Python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans = 1
        output = 0
        ran = collections.Counter(ransomNote)
        maga = collections.Counter(magazine)
        print(ran)
        print(maga)
        for k_ran in ran.keys():
            for k_maga in maga.keys():
                if k_ran == k_maga and ran[k_ran] <= maga[k_maga]:
                    output += 1
                    break
            if output == 0:
                ans = 0
            else:
                output = 0
        return bool(ans)
```
