from math import dist


# Question 1

def linear_scan(P,query):
    mini = float('inf')
    for point in P:
        d = dist(point,query)
        if d < mini:
            mini = d
            nearest = point
    return nearest

# Question 2

def partition(P, query, coord):
    L = []
    R = []
    
    for point in P:
        if point[coord] < query[coord]:
            L.append(point)
        elif point[coord] > query[coord]:
            R.append(point)    
            
    return L, R

def merge(L,R,coord):
    P = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i][coord] < R[j][coord]:
            P.append(L[i])
            i += 1
        else:
            P.append(R[j])
            j += 1
    if i < len(L):
        P.extend(L[i:])
    if j < len(R):
        P.extend(R[j:])
    return P

def merge_sort(P,coord):
    if len(P) <= 1:
        return P
    else:
        mid = len(P)//2
        L = merge_sort(P[:mid],coord)
        R = merge_sort(P[mid:],coord)
        return merge(L,R,coord)
    
# Question 3
def MoMSelect(P,coord,k):
    if len(P) < 10:
        sorted_P = merge_sort(P,coord)
        return sorted_P[k]
    
    medians = []
    for i in range(0,len(P),5):
        sorted_P5 = merge_sort(P[i:i+5],coord)
        m = len(sorted_P5) // 2
        medians.append(sorted_P5[m])
        
    p = MoMSelect(medians,coord,len(medians)//2)
    L, R = partition(P,p,coord)
    if k < len(L):
        return MoMSelect(L,coord,k)
    elif k > len(L):
        return MoMSelect(R,coord,k - len(L) - 1)
    else:
        return p
            
        
class KDTree:
    
    # Question 4
    def __init__ (self,P,coord = 0):
        
        if len(P) == 0:
            self.k = 0
            self.coord = 0
            self.rootPoint = None
            self.left = None
            self.right = None
            return
        
        self.k = len(P[0])
        self.coord = coord
        
        P = merge_sort(P,coord)
        m = len(P) // 2
        self.rootPoint = MoMSelect(P,coord,m)
        
        L, R = partition(P,self.rootPoint,coord)
        self.left = KDTree(L, (coord + 1) % self.k) if L else None
        self.right = KDTree(R, (coord + 1) % self.k) if R else None
                
    
    def __repr__(self):
        st = ""
        if not self.rootPoint is None:
            st += f"{self.rootPoint}(C{self.coord})("
            if not self.left is None:
                st += f"L:({self.left.__repr__()})"
            if not self.right is None:
                st += f"R:({self.right.__repr__()})"
            st += ")"
        return st
            
    def __str__(self, level=0):
        st = ""
        if self.rootPoint is None:
            st = "Empty"
        else:
            if level > 0:
                st = "|\t"*(level-1)+"|-->"
            st += f"{self.rootPoint} Coord= {self.coord}"
            if not self.left is None:
                st += f"\n {self.left.__str__(level+1)}"
            if not self.right is None:
                st += f"\n {self.right.__str__(level+1)}"
        return st

    def print_as_list(self):
        ll = [self.rootPoint]
        if not self.left is None:
            ll += self.left.give_list()
        if not self.right is None:
            ll += self.right.give_list()
        return ll
    
    # Question 5

    def NN_exhaustive_search(self, query):
        c = self.coord
        p = self.rootPoint
        med = p[c]
        if query[c] < med:
            if not self.left is None:
                cand = self.left.NN_exhaustive_search(query)
            else:
                cand = None
        else:
            if not self.right is None:
                cand = self.right.NN_exhaustive_search(query)
            else:
                cand = None
        if cand is not None and dist(query,cand) < dist(query,p):
            return cand
        return p
    # Question 6

    def NN_defeatist_search(self, query):
        
        c = self.coord
        p = self.rootPoint
        med = p[c]
        if query[c] <= med and self.left is not None:
            cand = self.left.NN_defeatist_search(query)
        elif query[c] > med and self.right is not None:
            cand = self.right.NN_defeatist_search(query)
        else:
            cand = None  

        if cand is not None and dist(query, cand) < dist(query, p):
            return cand
        return p
                     
   
    # Question 7

    def NN_backtracking_search(self,query, cand = None):
        p = self.rootPoint
        
        if cand is None or dist(query,p) < dist(query,cand):
            cand = p
        
        if self.left is None and self.right is None:
            return cand

        c = self.coord
        med = p[c]
        
        if query[c] <= med  and self.left is not None:
            cand = self.left.NN_backtracking_search(query, cand)
            if dist(query,cand) > abs(query[c] - med) and self.right is not None:
                cand = self.right.NN_backtracking_search(query, cand)
        elif query[c] > med and self.right is not None:
            cand = self.right.NN_backtracking_search(query, cand)
            if dist(query,cand) > abs(query[c] - med) and self.left is not None:
                cand = self.left.NN_backtracking_search(query, cand)
        
        return cand