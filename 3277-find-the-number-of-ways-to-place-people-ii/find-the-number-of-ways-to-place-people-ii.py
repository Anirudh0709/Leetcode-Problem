class Solution:
    def numberOfPairs(self, P: List[List[int]]) -> int:
        P.sort(key=lambda p:(-p[0], p[1]))
        ans, n=0, len(P)
        for i in range(n-1):
            a, ai=1<<31, P[i][1]
            for j in range(i+1, n):
                aj=P[j][1]
                if a>aj>=ai:
                    ans+=1
                    a=aj
                    if ai==aj: break
        return ans
        