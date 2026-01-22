class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        ans = ""
        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                if len(st) != 0:
                    ans += ch
                st.append(ch)
            else:
                st.pop()
                if len(st) != 0:
                    ans += ch
        return ans
