class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        st = []
        prev_time = 0

        for log in logs:
            id_str, typ, ts_str = log.split(":")
            iD = int(id_str)
            ts = int(ts_str)

            if typ == "start":
                if st :
                    res[st[-1]] += ts - prev_time
                st.append(iD)
                prev_time = ts

            else:
                res[st.pop()] += ts -prev_time + 1
                prev_time = ts +1
        return res
                