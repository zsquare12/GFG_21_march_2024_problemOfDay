if True:
    def findShortestPath(self, mat) -> int:
        # code here
        ans = []
        for i in range(len(mat)):
            path = [
                [[i, 0]],
            ]
            j = 0
            while True:

                #all done condition
                if path.count(0) == len(path):
                    break
                    
                #check paths again if not all done
                if j >= len(path):
                    j = 0

                bad_path = False
                cp = path[j]

                #if working on failed path
                if cp == 0:
                    j += 1; continue

                cpl = cp[-1]
                moves = [
                    [cpl[0], cpl[1]+1],
                    [cpl[0], cpl[1]-1],
                    [cpl[0]+1, cpl[1]],
                    [cpl[0]-1, cpl[1]],
                ]

                #boundary drop condition
                col_end = len(mat)
                row_end = len(mat[0])
                if not (0 <= cpl[0] and cpl[0] < col_end and 0 <= cpl[1] and cpl[1] < row_end):
                    path.pop(j)
                    j += 1; continue

                #mine drop condition
                for move in moves+[cpl]:
                    try:
                        if mat[move[0]][move[1]] == 0:
                            path.pop(j)
                            bad_path = True
                            break
                    except IndexError:
                        continue
                if bad_path:
                    j+=1;continue
                
                #repeat drop cocndition
                if cpl in cp[0:-1]:
                    path.pop(j)
                    j+=1; continue

                #reached safe destination condition
                if cpl[1] == row_end-1:
                    ans.append(len(path[j]))
                    path.pop(j)
                    j+=1; continue

                #no go first row, drop
                if (cpl[1] == 0) and (cpl[0] != cp[0][0]) and (len(cp) > 1) :
                    path.pop(j)
                    j+=1; continue


                #if passed all the above condition move it to next step

                for move in moves[1:]:
                    path.append(cp + [move])
                path[j].append(moves[0])

                j += 1
                
        if ans:
            return min(ans)
        else :
            return -1



test = [
    {
        "case" : [
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]
        ],
        "ans" : 6,
    },
    {
        "case" : [
            [1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1]
        ],
        "ans" : -1,
    },
]

for i in range(len(test)):
    myans = findShortestPath(0, test[i]['case'])
    print(f" case{i} \t {test[i]['ans']} \t {myans}")