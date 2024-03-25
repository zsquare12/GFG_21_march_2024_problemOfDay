if True:
    def NBitBinary(self, n):
        ans = ['1']
        while len(ans[0]) < n :
            for i in range(len(ans)):
                if ans[i].count('1') > ans[i].count('0') :
                    ans.append(ans[i] + '1')
                    ans[i] += '0'
                else :
                    ans[i] += '1'

        ans.sort(reverse=True)
        return ans


realans = NBitBinary(0, 5)

for i in realans:
    print(i)