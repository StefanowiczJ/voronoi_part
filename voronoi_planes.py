from math import sqrt
def add(a,b):
    j = len(a)
    return tuple(a[i]+b[i] for i in range(j))
    
def subs(a,b):
    j = len(a)
    return tuple(a[i]-b[i] for i in range(j))
    
def mul_scal(a,x):
    j = len(a)
    return tuple(a[i]*x for i in range(j))


def norm(a):
    sum_sq=0
    for i in range(len(a)):
        sum_sq = sum_sq+a[i]**2
        
    return sqrt(sum_sq)


def get_bisector(a,b):
    if norm(a)>norm(b):
        return get_bisector(b,a)
    s = add(a,mul_scal(subs(b,a),(1/2)))
    dist_s = norm(s)
    return (mul_scal(subs(b,a),1/norm(subs(b,a))),-dist_s)
    
def s_eq(point,hyperplane):
    s_eq=0
    for i in range(len(point)):
        s_eq = s_eq+point[i]*hyperplane[0][i]
    s_eq+=hyperplane[1]
    return s_eq
    
def get_borders(site,sites,D):
    for other in sites:
        if other!=site:
            hyperplane = get_bisector(site,other)
            ind = s_eq(site,hyperplane)
            D[site].append((hyperplane,ind))
            
def check_point(point,sites,D):
    resp = []
    for site in sites:
        in_site = True
        for hyperplane in D[site]:
            if not(s_eq(point,hyperplane[0])*hyperplane[1]>=0):
                in_site=False
                break
        if in_site == True:
            resp.append(site)
            
    return resp
    
def voronoi(sites,point):
    D = {}
    for site in sites:
        D[site] = []
    
    for site in sites:
        get_borders(site,sites,D)
        
    return check_point(point,sites,D)
    