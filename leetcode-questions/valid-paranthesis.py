class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        n = len(s)
        for i in range(n):
            ch = s[i]
            if ch == ')' or ch == ']' or ch == '}':
                if len(st) == 0:
                    return False
                top = st[-1]
                if (top == '(' and ch == ')') or (top == '[' and ch == ']') or (top == '{' and ch == '}'):
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)

        if len(st) == 0:
            return True
        return False
