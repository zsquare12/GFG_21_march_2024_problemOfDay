if True:
    def printArr(self, n, arr):
        # printing array elements with spaces
        # print(" ".join(map(str, arr)))
        pass
        

    def setToZero(self, n, arr):
        # setting all elements to zero
        print("0 "*n)
        

    def xor1ToN(self, n, arr):
        # doing xor with indices
        for i in range(n):
          e = arr[i]
          print(e^i, end=" ")
        print()
    
ar = list(range(1,11))
n = len(ar)
printArr(0, n, ar)
setToZero(0, n, ar)
xor1ToN(0, n, ar)