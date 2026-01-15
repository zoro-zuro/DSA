import operator
from math import trunc
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/": lambda a,b : trunc(a/b)
        }
        st = []

        for t in tokens:
            if t in ops:
                b = st.pop()
                a = st.pop()
                st.append(ops[t](a,b))
            else:
                st.append(int(t))
        return st[-1]




