from math import factorial

if True:
  def pairAndSum(self, n, arr):
    #code here
    bit_count = [0]*32

    for num in arr:
      for i in range(32):
        if ((num >> i) & 1) :
          bit_count[i] += 1
    
    resut_sum = 0
    for i in range(32):
      valuei = bit_count[i]
      if valuei >= 2:
        resut_sum += (valuei * (valuei - 1)) // 2 * (1 << i) 

    return int(resut_sum)

if __name__ == "__main__":
  ans = pairAndSum(0, 3, [5,10,15])
  ans2 = pairAndSum(0, 4, [10,20,30,40])
  print(ans, ans2)
