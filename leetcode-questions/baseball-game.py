class Solution:
    def calPoints(self, operations):
        st = []
        for i in range(len(operations)):
            ch = operations[i]
            if ch == "C":
                if len(st) != 0:
                    st.pop()
            elif ch == "+" and len(st) >= 2:
                one = st[-1]
                st.pop()
                two = st[-1]
                three = one + two
                st.append(one)
                st.append(three)
            elif ch == "D" and len(st) != 0:
                one = st[-1]
                st.append(2 * one)
            else:
                st.append(int(ch))

        sum = 0
        while len(st) != 0:
            sum += st[-1]
            st.pop()

        return sum
