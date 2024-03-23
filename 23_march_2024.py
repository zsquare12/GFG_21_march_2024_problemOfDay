#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        ans = [0,1]
        if n>1:
            for i in range(n-1):
                ans.append(int((ans[-1]+ans[-2])%(1e9+7)))
        
        return ans[0:n+1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends