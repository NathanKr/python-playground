from scipy.optimize import minimize

def eqn(x):
  return (x-1)**2 

x0=0
mymin = minimize(eqn, x0, method='BFGS')

print(mymin)

