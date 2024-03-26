
if True:
    def isAdditiveSequence(self, n):
        #code here
        alldone = False
        first = True
        nlast = len(n)
        
        ds1 = 0
        de1 = 1
        ds2 = 1
        de2 = 2

        #let's handle first case diffently 
        for i in range(1, nlast):
            for j in range(i+1, nlast):
                d1 = int(n[0:i])
                d2 = int(n[i:j])
                ad = d1+d2 
                try:
                    d3 = int(n[j: j+len(str(ad))])
                except IndexError:
                    break
                
                if d3 == ad:
                    de1 = i
                    ds2 = i
                    de2 = j
                    first = False
                    break
            if not first:
                break
                

        while not alldone:
            d1 = int(n[ds1: de1])
            d2 = int(n[ds2: de2])
            ad = d1 + d2
            
            digit = len(str(ad))
            ds3 = de2
            de3 = de2 + digit

            #terminating condition
            if de3 > nlast :
                return 0
            d3 = int(n[ds3: de3])

            if not d3 == ad:
                return 0
            
            if de3 == nlast:
                break

            
            ds1, de1 = ds2, de2
            ds2, de2 = ds3, de3

        return 1
    

test = [
    ['112', 1],
    ['111', 0],
    ['1123', 1],
    ['11235', 1],
    ['112358', 1],
    ["21214", 1],
    ["13236", 0],
    ["23968991", 1],
]

for i in test:
    print(f"{i[0]} \t\t {i[1]} \t {isAdditiveSequence(0, i[0])}")