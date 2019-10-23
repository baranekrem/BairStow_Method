import BairStow
 
# (4+x^0) + (-10*x^1) + (10*x^2) + (-5*x^3) + (1*x^4)
coeffs = [4, -10, 10, -5, 1]
r = 0.5
s = -0.5
epsilon = 10e-7
 
myRoots = BairStow.GetRoots(coeffs, r, s, epsilon)
 
for i in range(0, len(myRoots)):
    print("Root {:d} : {:.4f}".format((i + 1), (complex(myRoots[i]))))
