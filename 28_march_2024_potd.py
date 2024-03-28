if True:
    def findCity(self, n : int, m : int, edges : list[list[int]], distanceThreshold : int) -> int:
        # code here
        def city_within(city: int) :
            city_reached = {city : distanceThreshold} #it stores element list [city, distace_thereshold_remained]
            while True:
                update_city_reached  = False
                i=0
                while i<m:
                    e0, e1, e2 = edges[i]


                    if e0 in city_reached and e1 in city_reached:
                        reached_e0 = city_reached[e0]
                        reached_e1 = city_reached[e1]
                        dif01 = reached_e0 - e2
                        dif10 = reached_e1 - e2

                        if dif01 > reached_e1:
                            city_reached[e1] = dif01
                            update_city_reached = True
                        elif dif10 > city_reached[e0]:
                            city_reached[e0] = dif10
                            update_city_reached = True


                    elif e0 in city_reached:
                        reached_e0 = city_reached[e0]
                        if e2 <= reached_e0:
                            dif = reached_e0-e2
                            if e1 in city_reached:
                                reached_e1 = city_reached[e1]
                                if dif > reached_e1:
                                    city_reached[e1] = dif
                                    update_city_reached = True
                            else :
                                city_reached[e1] = dif
                                update_city_reached = True


                    elif e1 in city_reached:
                        reached_e1 = city_reached[e1]
                        if e2 <= reached_e1:
                            dif = reached_e1-e2
                            if e0 in city_reached:
                                reached_e0 = city_reached[e0]
                                if dif < reached_e0:
                                    city_reached[e0] = dif
                                    update_city_reached = True
                            else:
                                city_reached[e0] = dif
                                update_city_reached = True


                    i+=1
                
                if not update_city_reached:
                    break

            return city_reached
        
        all_city_reach = []
        for i in range(n):
            ans = city_within(i)
            all_city_reach.append(len(ans))
            
        
        min_city = min(all_city_reach)
        return n - all_city_reach[::-1].index(min_city) -1



test = [
    [
        4,4,4,
        [
            [0, 1, 3],
            [1, 2, 1], 
            [1, 3, 4],  
            [2, 3, 1]
        ]
    ],
    [
        5,6,2,
        [
            [0, 1, 2],
            [0, 4, 8],
            [1, 2, 3], 
            [1, 4, 2], 
            [2, 3, 1],
            [3, 4, 1]
        ]
    ],
    [
        6,6,4,
        [
            [0,1,1],
            [1,2,1],
            [2,3,1],
            [0,3,2],
            [3,4,1],
            [4,5,1]
        ]
    ],
    [
        34, 62, 161,
    [
        [33, 14, 62],
        [7, 3, 44],
        [19, 14, 65],
        [24, 11, 60],
        [17, 0, 68],
        [32, 6, 57],
        [32, 20, 23],
        [20, 3, 36],
        [33, 10, 42],
        [24, 2, 16],
        [13, 11, 83],
        [16, 0, 42],
        [30, 5, 5],
        [5, 1, 72],
        [22, 12, 93],
        [9, 3, 28],
        [29, 1, 20],
        [29, 15, 98],
        [23, 22, 34],
        [33, 9, 19],
        [31, 19, 9],
        [28, 20, 46],
        [32, 9, 91],
        [26, 5, 40],
        [27, 0, 24],
        [11, 3, 2],
        [25, 12, 95],
        [29, 11, 51],
        [29, 22, 86],
        [30, 7, 5],
        [26, 18, 28],
        [8, 5, 1],
        [16, 7, 6],
        [31, 13, 46],
        [20, 7, 28],
        [27, 23, 38],
        [30, 19, 21],
        [4, 1, 97],
        [25, 4, 51],
        [33, 27, 29],
        [26, 4, 8],
        [22, 0, 69],
        [32, 16, 24],
        [18, 12, 12],
        [28, 2, 33],
        [16, 4, 33],
        [17, 3, 24],
        [9, 1, 77],
        [13, 12, 66],
        [21, 12, 13],
        [25, 6, 59],
        [33, 23, 51],
        [29, 4, 8],
        [13, 5, 8],
        [29, 24, 4],
        [14, 10, 69],
        [23, 15, 33],
        [18, 15, 21],
        [30, 0, 90],
        [13, 6, 22],
        [29, 10, 31],
        [32, 1, 68]
    ]
    ]
]
ttest = test*250

from time import time

t1 = time()

for i in range(len(ttest)):
    case = ttest[i]
    mything = findCity(0, case[0], case[1], case[3], case[2])
    # print(f" testcase {i} output {mything}")

print(time()-t1)