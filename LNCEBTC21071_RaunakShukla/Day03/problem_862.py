class Solution:
    def shortestSubarray(self, nums, k) :
        q, pre, ans = deque([0]), [0], float('inf')

        for x in nums:
            pre.append(pre[-1] + x)
            i = len(pre) - 1

            while q and pre[i] - pre[q[0]] >= k:
                ans = min(ans, i - q.popleft())

            while q and pre[i] <= pre[q[-1]]:
                q.pop()

            q.append(i)
        return ans if ans != float('inf') else -1        