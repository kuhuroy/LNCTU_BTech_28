from collections import deque

class Solution:
    def shortestSubarray(self, a, k):
        s=[0]; q=deque(); ans=10**9
        for x in a:s+=[s[-1]+x]
        for i,x in enumerate(s):
            while q and x-s[q[0]]>=k: ans=min(ans,i-q.popleft())
            while q and x<=s[q[-1]]: q.pop()
            q.append(i)
        return ans if ans<10**9 else -1
