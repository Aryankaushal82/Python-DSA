class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        st = []
        ans = ""
        found = False

        for i in range(len(word)):
            if not found:
                st.append(word[i])
                if word[i] == ch:
                    found = True
                    while st:
                        ans += st.pop()
            else:
                ans += word[i]

        if not found:
            return word

        return ans