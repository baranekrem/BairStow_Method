import math
import cmath
 
def GetRoots(a, r, s, err):
    n = (len(a) - 1)
 
    roots = [0]*n
    rootIndex = 0
 
    b = [0]*(len(a))
    c = [0]*(len(a))
 
    b[n] = a[n]
    b[n - 1] = a[n - 1] + r * b[n]
 
    c[n] = b[n]
    c[n - 1] = b[n - 1] + r * c[n]
 
    while n > 2:
        ep = 1
        c[n] = b[n] = a[n]
        while (ep > err):
            b[n - 1] = a[n - 1] + r * b[n]
            c[n - 1] = b[n - 1] + r * c[n]
 
            for i in range(n - 2, -1, -1):
                b[i] = a[i] + r * b[i + 1] + s * b[i + 2]
                c[i] = b[i] + r * c[i + 1] + s * c[i + 2]
 
            b[0] = a[0] + r * b[1] + s * b[2]
 
            delta_r = (b[0] * c[3] - b[1] * c[2]) / (c[2] * c[2] - c[1] * c[3])
            delta_s = (c[1] * b[1] - c[2] * b[0]) / (c[2] * c[2] - c[1] * c[3])
 
            r += delta_r
            s += delta_s
 
            ep = math.sqrt(delta_r * delta_r + delta_s * delta_s)
 
        roots[rootIndex] = (r + cmath.sqrt(r * r + 4 * s)) / 2
        roots[rootIndex + 1] = (r - cmath.sqrt(r * r + 4 * s)) / 2
 
        rootIndex += 2
 
        n -= 2
 
        for i in range(0, n + 1):
            a[i] = b[i + 2]
 
    if(n == 2):
        r = -a[1] / a[2]
        s = -a[0] / a[2]
 
        roots[rootIndex] = (r + cmath.sqrt(r * r + 4 * s)) / 2
        roots[rootIndex + 1] = (r - cmath.sqrt(r * r + 4 * s)) / 2
 
    if(n == 1):
        roots[rootIndex] = -a[0] / a[1]
 
    return (roots)
