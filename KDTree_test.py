import KDTree as kdt
import time
import math
import matplotlib.pyplot as plt
import numpy as np

def test_linear_scan():
    if kdt.linear_scan([[0]],[0]) is None:
        print("Skipping function linear_scan() –- not implemented")
        return False
    else:
        print("Testing linear_scan()")

    isOk = True
    inp = [ \
        [[0.1,0.1], [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]], \
        [[0,0], [[0, 4], [1, 3], [2, 2], [3, 1]]], \
        [[0.1,0.1], [[3, 0], [1, 2], [4, 1], [2, 3], [0, 4]]], \
        [[0.1,0.1,0.1], [[36, 30, 17], [29, 28, 46], [15, 41, 28], [21, 24, 36], [35, 11,27], [4, 32, 49], [13, 0, 41], [27, 16, 20], [31, 7, 39], [11, 9, 6], [14, 17, 24], [7,26, 9], [39, 44, 42], [22, 18, 40], [33, 12, 0], [18, 38, 45], [38, 29, 12], [8,46, 29], [26, 21, 15], [25, 36, 21], [32, 31, 10], [12, 27, 37], [48, 40, 31], [41, 39, 34], [19, 25, 44], [3, 45, 43], [43, 8, 32], [6, 1, 33], [5, 22, 19], [46,43, 35], [49, 3, 7], [45, 33,3], [40, 4, 14], [1, 37, 23], [0, 14, 30], [10, 20,26], [42, 10, 22], [34, 34, 2], [20, 5, 16], [17, 19, 4], [16, 6, 25], [23, 2,47], [28, 42, 18], [2, 23, 5], [30, 35, 11], [47, 49, 13], [24, 13, 38], [9, 47,1], [37, 48, 8], [44, 15, 48]]] \
        ]
               
    outp = [[0, 0], [2, 2], [1,2], [11, 9, 6]]
    
    for i in range(0,len(inp)):
        query = inp[i][0]
        P = inp[i][1]
        if kdt.linear_scan(P,query) == outp[i]:
            print(f"OK test {i+1}")
        else:
            isOk = False
            print(f"Error in test {i+1}")
            print(f"Input: linear_scan({P},{query})")
            print(f"Expected: {outp[i]}")
    return isOk

def test_partition():
    if kdt.partition([[0]],[0],0) is None:
        print("Skipping function partition() –- not implemented")
        return False
    else:
        print("Testing partition()")

    isOk = True
    inp = [ \
                [[1,1], 0,[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]],\
                [[1,3], 0, [[0, 4], [1, 3], [2, 2], [3, 1]]],\
                [[3,1], 1, [[0, 4], [1, 3], [2, 2], [3, 1]]],\
                [[32, 31, 10], 2, [[36, 30, 17], [29, 28, 46], [15, 41, 28], [21, 24, 36], [35, 11,27], [4, 32, 49], [13, 0, 41], [27, 16, 20], [31, 7, 39], [11, 9, 6], [14, 17, 24], [7,26, 9], [39, 44, 42], [22, 18, 40], [33, 12, 0], [18, 38, 45], [38, 29, 12], [8,46, 29], [26, 21, 15], [25, 36, 21], [32, 31, 10], [12, 27, 37], [48, 40, 31], [41, 39, 34], [19, 25, 44], [3, 45, 43], [43, 8, 32], [6, 1, 33], [5, 22, 19], [46,43, 35], [49, 3, 7], [45, 33,3], [40, 4, 14], [1, 37, 23], [0, 14, 30], [10, 20,26], [42, 10, 22], [34, 34, 2], [20, 5, 16], [17, 19, 4], [16, 6, 25], [23, 2,47], [28, 42, 18], [2, 23, 5], [30, 35, 11], [47, 49, 13], [24, 13, 38], [9, 47,1], [37, 48, 8], [44, 15, 48]]]\
        ]
               
    outp = [ \
        [[[0, 0]], [[2, 2], [3, 3], [4, 4]]],\
        [[[0, 4]], [[2, 2], [3, 1]]],\
        [[], [[2, 2], [1, 3], [0, 4]]],\
        [[[33, 12, 0], [9, 47, 1], [34, 34, 2], [45, 33, 3], [17, 19, 4], [2, 23, 5], [11, 9, 6], [49, 3, 7], [37, 48, 8], [7, 26, 9]], [[30, 35, 11], [38, 29, 12], [47, 49, 13], [40, 4, 14], [26, 21, 15], [20, 5, 16], [36, 30, 17], [28, 42, 18], [5, 22, 19], [27, 16, 20], [25, 36, 21], [42, 10, 22], [1, 37, 23], [14, 17, 24], [16, 6, 25], [10, 20, 26], [35, 11, 27], [15, 41, 28], [8, 46, 29], [0, 14, 30], [48, 40, 31], [43, 8, 32], [6, 1, 33], [41, 39, 34], [46, 43, 35], [21, 24, 36], [12, 27, 37], [24, 13, 38], [31, 7, 39], [22, 18, 40], [13, 0, 41], [39, 44, 42], [3, 45, 43], [19, 25, 44], [18, 38, 45], [29, 28, 46], [23, 2, 47], [44, 15, 48], [4, 32, 49]]]
    ]
    
    for i in range(0,len(inp)):
        
        query = inp[i][0]
        coord = inp[i][1]
        P = inp[i][2]
        L,R = kdt.partition(P,query,coord)
        L.sort(key=lambda elem : elem[coord])
        R.sort(key=lambda elem : elem[coord])
        if L == outp[i][0] and R == outp[i][1]:
            print(f"OK test {i+1}")
        else:
            isOk = False
            print(f"Error in test {i+1}")
            print(f"Input: Partition({P},{query},{coord})")
            print(f"Expected: {outp[i][0]}")
    return isOk


def test_MoMSelect():
    if kdt.MoMSelect([[0]],0,0) is None:
        print("Skipping function MoMSelect() –- not implemented")
        return False
    else:
        print("Testing MoMSelect()")

    isOk = True
    inp = [ \
                [0, 4, [[0, 4], [1, 3], [2, 2], [3, 1], [4,5], [-1,-1],[10,10]]],\
                [1, 4, [[0, 4], [1, 3], [2, 2], [3, 1], [4,5], [-1,-1],[10,10]]],\
                [1, 23, [[36, 30, 17], [29, 28, 46], [15, 41, 28], [21, 24, 36], [35, 11,27], [4, 32, 49], [13, 0, 41], [27, 16, 20], [31, 7, 39], [11, 9, 6], [14, 17, 24], [7,26, 9], [39, 44, 42], [22, 18, 40], [33, 12, 0], [18, 38, 45], [38, 29, 12], [8,46, 29], [26, 21, 15], [25, 36, 21], [32, 31, 10], [12, 27, 37], [48, 40, 31], [41, 39, 34], [19, 25, 44], [3, 45, 43], [43, 8, 32], [6, 1, 33], [5, 22, 19], [46,43, 35], [49, 3, 7], [45, 33,3], [40, 4, 14], [1, 37, 23], [0, 14, 30], [10, 20,26], [42, 10, 22], [34, 34, 2], [20, 5, 16], [17, 19, 4], [16, 6, 25], [23, 2,47], [28, 42, 18], [2, 23, 5], [30, 35, 11], [47, 49, 13], [24, 13, 38], [9, 47,1], [37, 48, 8], [44, 15, 48]]],\
                [0, 25, [[36, 30, 17], [29, 28, 46], [15, 41, 28], [21, 24, 36], [35, 11,27], [4, 32, 49], [13, 0, 41], [27, 16, 20], [31, 7, 39], [11, 9, 6], [14, 17, 24], [7,26, 9], [39, 44, 42], [22, 18, 40], [33, 12, 0], [18, 38, 45], [38, 29, 12], [8,46, 29], [26, 21, 15], [25, 36, 21], [32, 31, 10], [12, 27, 37], [48, 40, 31], [41, 39, 34], [19, 25, 44], [3, 45, 43], [43, 8, 32], [6, 1, 33], [5, 22, 19], [46,43, 35], [49, 3, 7], [45, 33,3], [40, 4, 14], [1, 37, 23], [0, 14, 30], [10, 20,26], [42, 10, 22], [34, 34, 2], [20, 5, 16], [17, 19, 4], [16, 6, 25], [23, 2,47], [28, 42, 18], [2, 23, 5], [30, 35, 11], [47, 49, 13], [24, 13, 38], [9, 47,1], [37, 48, 8], [44, 15, 48]]]\
        ]
               
    outp = [ \
                 [[3, 1]],\
                 [[0, 4]],\
                 [[2, 23, 5]],\
                 [[25, 36, 21]]\
    ]
    
    for i in range(0,len(inp)):
        
        coord = inp[i][0]
        k = inp[i][1]
        P = inp[i][2]
        el = kdt.MoMSelect(P,coord,k)
        if el == outp[i][0]:
            print(f"OK test {i+1}")
        else:
            isOk = False
            print(f"Error in test {i+1}")
            print(f"Input: MoMSelect({P},{coord},{k})")
            print(f"Expected: {outp[i][0]}")
    return isOk


def test_init_KDTree():
    tst = kdt.KDTree([[0]])
    if not hasattr(tst,"k"):
        print("Skipping function KDTree.__init__() –- not implemented")
        return False
    else:
        print("Testing KDTree.__init__()")

    isOk = True
    inp = [ \
                [[[2,3],[4,7],[5,4],[7,2],[8,1],[9,6],[9.1,9]]],\
                [[[12], [19], [25], [3], [5], [17], [24], [23], [7], [9], [11], [28], [2], [26], [8], [21], [15], [20], [18], [27], [14], [1], [16], [22], [29], [0], [30], [10], [4], [6], [13]]],\
                [[[36, 30, 17], [29, 28, 46], [15, 41, 28], [21, 24, 36], [35, 11,27], [4, 32, 49], [13, 0, 41], [27, 16, 20], [31, 7, 39], [11, 9, 6], [14, 17, 24], [7,26, 9], [39, 44, 42], [22, 18, 40], [33, 12, 0], [18, 38, 45], [38, 29, 12], [8,46, 29], [26, 21, 15], [25, 36, 21], [32, 31, 10], [12, 27, 37], [48, 40, 31], [41, 39, 34], [19, 25, 44], [3, 45, 43], [43, 8, 32], [6, 1, 33], [5, 22, 19], [46,43, 35], [49, 3, 7], [45, 33,3], [40, 4, 14], [1, 37, 23], [0, 14, 30], [10, 20,26], [42, 10, 22], [34, 34, 2], [20, 5, 16], [17, 19, 4], [16, 6, 25], [23, 2,47], [28, 42, 18], [2, 23, 5], [30, 35, 11], [47, 49, 13], [24, 13, 38], [9, 47,1], [37, 48, 8], [44, 15, 48]]],\
                [[[37, 34, 23, 24], [46, 11, 21, 3], [33, 15, 31, 38], [26, 16, 15, 19], [25, 26, 13, 47], [35, 36, 41, 2], [27, 41, 43, 25], [5, 8, 20, 29], [47, 28, 30, 44], [10, 25, 18, 27], [17, 21, 28, 20], [8, 33, 38, 14], [41, 46, 26, 28], [7, 9, 39, 12], [31, 40, 9, 43], [18, 22, 6, 46], [34, 27, 1, 45], [19, 29, 5, 39], [16, 42, 22, 26], [43, 35, 2, 33], [42, 17, 33, 36], [45, 4, 14, 22], [28, 2, 42, 4], [2, 44, 0, 5], [36, 30, 24, 18], [29, 37, 29, 7], [32, 45, 25, 6], [22, 31, 8, 17], [38, 39, 11, 9], [12, 7, 46, 11], [6, 6, 36, 32], [20, 5, 12, 10], [39, 10, 32, 13], [3, 3, 44, 1], [21, 23, 10, 37], [11, 0, 4, 35], [30, 19, 3, 16], [23, 47, 40, 23], [24, 43, 19, 15], [14, 12, 7, 30], [13, 1, 34, 40], [15, 24, 47, 42], [1, 38, 17, 8], [40, 18, 37, 0], [0, 20, 27, 31], [9, 13, 35, 41], [4, 32, 45, 34], [44, 14, 16, 21]]]
                ]
               
    outp = [ \
                 ["[7, 2] Coord= 0\n |-->[5, 4] Coord= 1\n |\t|-->[2, 3] Coord= 0\n |\t|-->[4, 7] Coord= 0\n |-->[9, 6] Coord= 1\n |\t|-->[8, 1] Coord= 0\n |\t|-->[9.1, 9] Coord= 0"],["[15] Coord= 0\n |-->[7] Coord= 0\n |\t|-->[3] Coord= 0\n |\t|\t|-->[1] Coord= 0\n |\t|\t|\t|-->[0] Coord= 0\n |\t|\t|\t|-->[2] Coord= 0\n |\t|\t|-->[5] Coord= 0\n |\t|\t|\t|-->[4] Coord= 0\n |\t|\t|\t|-->[6] Coord= 0\n |\t|-->[11] Coord= 0\n |\t|\t|-->[9] Coord= 0\n |\t|\t|\t|-->[8] Coord= 0\n |\t|\t|\t|-->[10] Coord= 0\n |\t|\t|-->[13] Coord= 0\n |\t|\t|\t|-->[12] Coord= 0\n |\t|\t|\t|-->[14] Coord= 0\n |-->[23] Coord= 0\n |\t|-->[19] Coord= 0\n |\t|\t|-->[17] Coord= 0\n |\t|\t|\t|-->[16] Coord= 0\n |\t|\t|\t|-->[18] Coord= 0\n |\t|\t|-->[21] Coord= 0\n |\t|\t|\t|-->[20] Coord= 0\n |\t|\t|\t|-->[22] Coord= 0\n |\t|-->[27] Coord= 0\n |\t|\t|-->[25] Coord= 0\n |\t|\t|\t|-->[24] Coord= 0\n |\t|\t|\t|-->[26] Coord= 0\n |\t|\t|-->[29] Coord= 0\n |\t|\t|\t|-->[28] Coord= 0\n |\t|\t|\t|-->[30] Coord= 0"],["[25, 36, 21] Coord= 0\n |-->[5, 22, 19] Coord= 1\n |\t|-->[0, 14, 30] Coord= 2\n |\t|\t|-->[16, 6, 25] Coord= 0\n |\t|\t|\t|-->[14, 17, 24] Coord= 1\n |\t|\t|\t|\t|-->[11, 9, 6] Coord= 2\n |\t|\t|\t|\t|-->[10, 20, 26] Coord= 2\n |\t|\t|\t|-->[17, 19, 4] Coord= 1\n |\t|\t|\t|\t|-->[20, 5, 16] Coord= 2\n |\t|\t|-->[22, 18, 40] Coord= 0\n |\t|\t|\t|-->[6, 1, 33] Coord= 1\n |\t|\t|\t|\t|-->[13, 0, 41] Coord= 2\n |\t|\t|\t|-->[24, 13, 38] Coord= 1\n |\t|\t|\t|\t|-->[23, 2, 47] Coord= 2\n |\t|-->[21, 24, 36] Coord= 2\n |\t|\t|-->[8, 46, 29] Coord= 0\n |\t|\t|\t|-->[7, 26, 9] Coord= 1\n |\t|\t|\t|\t|-->[2, 23, 5] Coord= 2\n |\t|\t|\t|\t|-->[1, 37, 23] Coord= 2\n |\t|\t|\t|-->[9, 47, 1] Coord= 1\n |\t|\t|\t|\t|-->[15, 41, 28] Coord= 2\n |\t|\t|-->[12, 27, 37] Coord= 0\n |\t|\t|\t|-->[3, 45, 43] Coord= 1\n |\t|\t|\t|\t|-->[4, 32, 49] Coord= 2\n |\t|\t|\t|-->[18, 38, 45] Coord= 1\n |\t|\t|\t|\t|-->[19, 25, 44] Coord= 2\n |-->[36, 30, 17] Coord= 1\n |\t|-->[42, 10, 22] Coord= 2\n |\t|\t|-->[38, 29, 12] Coord= 0\n |\t|\t|\t|-->[27, 16, 20] Coord= 1\n |\t|\t|\t|\t|-->[33, 12, 0] Coord= 2\n |\t|\t|\t|\t|-->[26, 21, 15] Coord= 2\n |\t|\t|\t|-->[40, 4, 14] Coord= 1\n |\t|\t|\t|\t|-->[49, 3, 7] Coord= 2\n |\t|\t|-->[35, 11, 27] Coord= 0\n |\t|\t|\t|-->[29, 28, 46] Coord= 1\n |\t|\t|\t|\t|-->[31, 7, 39] Coord= 2\n |\t|\t|\t|-->[44, 15, 48] Coord= 1\n |\t|\t|\t|\t|-->[43, 8, 32] Coord= 2\n |\t|-->[47, 49, 13] Coord= 2\n |\t|\t|-->[34, 34, 2] Coord= 0\n |\t|\t|\t|-->[30, 35, 11] Coord= 1\n |\t|\t|\t|\t|-->[32, 31, 10] Coord= 2\n |\t|\t|\t|-->[37, 48, 8] Coord= 1\n |\t|\t|\t|\t|-->[45, 33, 3] Coord= 2\n |\t|\t|-->[41, 39, 34] Coord= 0\n |\t|\t|\t|-->[39, 44, 42] Coord= 1\n |\t|\t|\t|\t|-->[28, 42, 18] Coord= 2\n |\t|\t|\t|-->[46, 43, 35] Coord= 1\n |\t|\t|\t|\t|-->[48, 40, 31] Coord= 2"],["[24, 43, 19, 15] Coord= 0\n |-->[18, 22, 6, 46] Coord= 1\n |\t|-->[13, 1, 34, 40] Coord= 2\n |\t|\t|-->[14, 12, 7, 30] Coord= 3\n |\t|\t|\t|-->[17, 21, 28, 20] Coord= 0\n |\t|\t|\t|\t|-->[5, 8, 20, 29] Coord= 1\n |\t|\t|\t|\t|-->[20, 5, 12, 10] Coord= 1\n |\t|\t|\t|-->[11, 0, 4, 35] Coord= 0\n |\t|\t|\t|\t|-->[0, 20, 27, 31] Coord= 1\n |\t|\t|-->[7, 9, 39, 12] Coord= 3\n |\t|\t|\t|-->[12, 7, 46, 11] Coord= 0\n |\t|\t|\t|\t|-->[3, 3, 44, 1] Coord= 1\n |\t|\t|\t|-->[9, 13, 35, 41] Coord= 0\n |\t|\t|\t|\t|-->[6, 6, 36, 32] Coord= 1\n |\t|-->[10, 25, 18, 27] Coord= 2\n |\t|\t|-->[22, 31, 8, 17] Coord= 3\n |\t|\t|\t|-->[2, 44, 0, 5] Coord= 0\n |\t|\t|\t|\t|-->[1, 38, 17, 8] Coord= 1\n |\t|\t|\t|-->[21, 23, 10, 37] Coord= 0\n |\t|\t|\t|\t|-->[19, 29, 5, 39] Coord= 1\n |\t|\t|-->[16, 42, 22, 26] Coord= 3\n |\t|\t|\t|-->[23, 47, 40, 23] Coord= 0\n |\t|\t|\t|\t|-->[8, 33, 38, 14] Coord= 1\n |\t|\t|\t|-->[15, 24, 47, 42] Coord= 0\n |\t|\t|\t|\t|-->[4, 32, 45, 34] Coord= 1\n |-->[34, 27, 1, 45] Coord= 1\n |\t|-->[46, 11, 21, 3] Coord= 2\n |\t|\t|-->[44, 14, 16, 21] Coord= 3\n |\t|\t|\t|-->[30, 19, 3, 16] Coord= 0\n |\t|\t|\t|\t|-->[26, 16, 15, 19] Coord= 1\n |\t|\t|\t|-->[45, 4, 14, 22] Coord= 0\n |\t|\t|\t|\t|-->[25, 26, 13, 47] Coord= 1\n |\t|\t|-->[39, 10, 32, 13] Coord= 3\n |\t|\t|\t|-->[40, 18, 37, 0] Coord= 0\n |\t|\t|\t|\t|-->[28, 2, 42, 4] Coord= 1\n |\t|\t|\t|-->[42, 17, 33, 36] Coord= 0\n |\t|\t|\t|\t|-->[33, 15, 31, 38] Coord= 1\n |\t|-->[32, 45, 25, 6] Coord= 2\n |\t|\t|-->[37, 34, 23, 24] Coord= 3\n |\t|\t|\t|-->[38, 39, 11, 9] Coord= 0\n |\t|\t|\t|\t|-->[36, 30, 24, 18] Coord= 1\n |\t|\t|\t|-->[43, 35, 2, 33] Coord= 0\n |\t|\t|\t|\t|-->[31, 40, 9, 43] Coord= 1\n |\t|\t|-->[27, 41, 43, 25] Coord= 3\n |\t|\t|\t|-->[35, 36, 41, 2] Coord= 0\n |\t|\t|\t|\t|-->[29, 37, 29, 7] Coord= 1\n |\t|\t|\t|-->[47, 28, 30, 44] Coord= 0\n |\t|\t|\t|\t|-->[41, 46, 26, 28] Coord= 1"]]
    
    for i in range(0,len(inp)):
        
        P = inp[i][0]
        tree = kdt.KDTree(P)
        if tree.__str__() == outp[i][0]:
            print(f"OK test {i+1}")
        else:
            isOk = False
            print(f"Error in test {i+1}")
            print(f"Input: __init__({P})")
            print("Expected:")
            print(outp[i][0])
    return isOk



def test_NN_exhaustive_search():
    tst = kdt.KDTree([[0]])
    if not hasattr(tst,"k") or tst.NN_exhaustive_search([0]) is None:
        print("Skipping function KDTree.NN_exhaustive_search() –- not implemented")
        return False
    else:
        print("Testing KDTree.NN_exhaustive_search()")

    isOk = True
    inp = [ \
                [[0.1,0.1], [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]],\
                [[0,0], [[0, 4], [1, 3], [2, 2], [3, 1]]],\
                [[0.1,0.1], [[3, 0], [1, 2], [4, 1], [2, 3], [0, 4]]],\
                [[0.1,0.1,0.1], [[36, 30, 17], [29, 28, 46], [15, 41, 28], [21, 24, 36], [35, 11,27], [4, 32, 49], [13, 0, 41], [27, 16, 20], [31, 7, 39], [11, 9, 6], [14, 17, 24], [7,26, 9], [39, 44, 42], [22, 18, 40], [33, 12, 0], [18, 38, 45], [38, 29, 12], [8,46, 29], [26, 21, 15], [25, 36, 21], [32, 31, 10], [12, 27, 37], [48, 40, 31], [41, 39, 34], [19, 25, 44], [3, 45, 43], [43, 8, 32], [6, 1, 33], [5, 22, 19], [46,43, 35], [49, 3, 7], [45, 33,3], [40, 4, 14], [1, 37, 23], [0, 14, 30], [10, 20,26], [42, 10, 22], [34, 34, 2], [20, 5, 16], [17, 19, 4], [16, 6, 25], [23, 2,47], [28, 42, 18], [2, 23, 5], [30, 35, 11], [47, 49, 13], [24, 13, 38], [9, 47,1], [37, 48, 8], [44, 15, 48]]]\
                ]
               
    outp = [ \
                 [[0, 0]],\
                 [[2, 2]],\
                 [[1, 2]],\
                 [[11, 9, 6]]\
                 ]
    
    for i in range(0,len(inp)):
        
        query = inp[i][0]
        P = inp[i][1]
        tree = kdt.KDTree(P)
        if tree.NN_exhaustive_search(query) == outp[i][0]:
            print(f"OK test {i+1}")
        else:
            isOk = False
            print(f"Error in test {i+1}")
            print(f"Input: NN_exhaustive_search({query}) \n points: {P}")
            print(f"Expected: {outp[i][0]}")
    return isOk


def test_NN_defeatist_search():
    tst = kdt.KDTree([[0]])
    if not hasattr(tst,"k") or tst.NN_defeatist_search([0]) is None:
        print("Skipping function KDTree.NN_defeatist_search() –- not implemented")
        return False
    else:
        print("Testing KDTree.NN_defeatist_search()")

    isOk = True
    inp = [ \
                [[0,0], [[0, 4], [1, 3], [2, 2], [3, 1]]],\
                [[0,0], [[0.3,1.1],[1,1],[1.1,0]]],\
                [[0,0], [[1.1,0.3],[1,1],[0,1.1]]],\
                [[5,0], [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [5, 5]]]\
                ]
               
    outp = [ \
                 [[2, 2]],\
                 [[0.3, 1.1]],\
                 [[0, 1.1]],\
                 [[5, 5]]\
                 ]
    
    for i in range(0,len(inp)):
        
        query = inp[i][0]
        P = inp[i][1]
        tree = kdt.KDTree(P)
        print("My output: ", tree.NN_defeatist_search(query))
        if tree.NN_defeatist_search(query) == outp[i][0]:
            print(f"OK test {i+1}")
        else:
            isOk = False
            print(f"Error in test {i+1}")
            print(f"Input: NN_defeatist_search({query}) \n points: {P}")
            print(f"Expected: {outp[i][0]}")
    return isOk

def test_NN_backtracking_search():
    tst = kdt.KDTree([[0]])
    if not hasattr(tst,"k") or tst.NN_backtracking_search([0]) is None:
        print("Skipping function KDTree.NN_backtracking_search() –- not implemented")
        return False
    else:
        print("Testing KDTree.NN_backtracking_search()")

    isOk = True
    inp = [ \
                [[0.1,0.1], [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]],\
                [[0,0], [[0, 4], [1, 3], [2, 2], [3, 1]]],\
                [[0.1,0.1], [[3, 0], [1, 2], [4, 1], [2, 3], [0, 4]]],\
                [[0.1,0.1,0.1], [[36, 30, 17], [29, 28, 46], [15, 41, 28], [21, 24, 36], [35, 11,27], [4, 32, 49], [13, 0, 41], [27, 16, 20], [31, 7, 39], [11, 9, 6], [14, 17, 24], [7,26, 9], [39, 44, 42], [22, 18, 40], [33, 12, 0], [18, 38, 45], [38, 29, 12], [8,46, 29], [26, 21, 15], [25, 36, 21], [32, 31, 10], [12, 27, 37], [48, 40, 31], [41, 39, 34], [19, 25, 44], [3, 45, 43], [43, 8, 32], [6, 1, 33], [5, 22, 19], [46,43, 35], [49, 3, 7], [45, 33,3], [40, 4, 14], [1, 37, 23], [0, 14, 30], [10, 20,26], [42, 10, 22], [34, 34, 2], [20, 5, 16], [17, 19, 4], [16, 6, 25], [23, 2,47], [28, 42, 18], [2, 23, 5], [30, 35, 11], [47, 49, 13], [24, 13, 38], [9, 47,1], [37, 48, 8], [44, 15, 48]]],\
                [[0,0], [[0.3,1.1],[1,1],[1.1,0]]],\
                [[0,0], [[1.1,0.3],[1,1],[0,1.1]]],\
                [[5,0], [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [5, 5]]]\
                ]
               
    outp = [ \
                 [[0, 0]],\
                 [[2, 2]],\
                 [[1, 2]],\
                 [[11, 9, 6]],\
                 [[1.1,0]],\
                 [[0,1.1]],\
                 [[6,0]]\
                 ]
    
    for i in range(0,len(inp)):
        
        query = inp[i][0]
        P = inp[i][1]
        tree = kdt.KDTree(P)
        if tree.NN_backtracking_search(query) == outp[i][0]:
            print(f"OK test {i+1}")
        else:
            isOk = False
            print(f"Error in test {i+1}")
            print(f"Input: NN_backtracking_search({query}) \n points: {P}")
            print(f"Expected: {outp[i][0]}")
    return isOk


def testTimeBack(tree, queries):
    start_time = time.time()
    for el in queries:
        tree.NN_backtracking_search(el)
    end_time = time.time()
    time_alg = (end_time - start_time) / len(queries) * 1000
    return time_alg

def testTimeExh(tree, queries):
    start_time = time.time()
    for el in queries:
        tree.NN_exhaustive_search(el)
    end_time = time.time()
    time_alg = (end_time - start_time) / len(queries) * 1000
    return time_alg


def testTimeRandom():
    print("Counting until 15")
    sizes,timeBack,timeExh = [],[],[]
    for i in range(1,9):
        size = math.ceil(10**(i/3))
        print(i,size)
        database = (np.random.rand(size,2)).tolist()
        queries = (np.random.rand(1000,2)).tolist()
        tree = kdt.KDTree(database)
        sizes.append(i)
        timeBack.append(testTimeBack(tree,queries))
        timeExh.append(testTimeExh(tree,queries))

    for i in range(9,16):
        size = math.ceil(10**(i/3))
        print(i,size)
        database = (np.random.rand(size,2)).tolist()
        queries = (np.random.rand(1000,2)).tolist()
        tree = kdt.KDTree(database)
        sizes.append(i)
        timeBack.append(testTimeBack(tree,queries))

    plt.plot(sizes,timeBack, color='red', label='Backtracking')
    plt.plot(sizes[:len(timeExh)],timeExh, color='blue', label='Exhaustive')

    plt.legend(loc='upper left')

    plt.xlabel('Log of size of database')
    plt.ylabel('Time')
    plt.title('Random points in cube')
    plt.show()

def testTimeCircle():
    print("Counting until 11")
    sizes,timeBack,timeExh = [],[],[]
    mean = [0,0,0]
    cov = [[1,0,0],[0,1,0],[0,0,1]]
    for i in range(1,12):
        size = math.ceil(10**(i/3))
        print(i,size)
        rndNorm = (np.random.multivariate_normal(mean,cov,size))
        database = list(map(lambda x : (1/np.linalg.norm(x)*x).tolist(),rndNorm))
        queries = (np.random.rand(1000,3)).tolist()
        tree = kdt.KDTree(database)
        sizes.append(size)
        timeBack.append(testTimeBack(tree,queries))
        timeExh.append(testTimeExh(tree,queries))


    plt.plot(sizes,timeBack, color='red', label='Backtracking')
    plt.plot(sizes[:len(timeExh)],timeExh, color='blue', label='Exhaustive')

    plt.legend(loc='upper left')

    plt.xlabel('Size of database')
    plt.ylabel('Time')
    plt.title('Database = Random points in sphere, Queries = Random points in cube')
    plt.show()

iseverythingok = True
    
# Test question 1
iseverythingok = iseverythingok and test_linear_scan()
# Test question 2
iseverythingok = iseverythingok and test_partition()
# Test question 3
iseverythingok = iseverythingok and test_MoMSelect()
# Test question 4
iseverythingok = iseverythingok and test_init_KDTree()
# Test question 5
iseverythingok = iseverythingok and test_NN_exhaustive_search()
# Test question 6
iseverythingok = iseverythingok and test_NN_defeatist_search()
# Test question 7
iseverythingok = iseverythingok and test_NN_backtracking_search()

# Question 8
if iseverythingok:
    # Generate graphics
    print("You passed every test, generating graphics")
    testTimeRandom()
    testTimeCircle()
    print("See you next week!")
