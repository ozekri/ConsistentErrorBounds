import numpy as np
import proj_exp_cone as pe


def proj_v2(x):
      return [0,x[1],x[2]]

def isinC(v):
    if v[2] <=0.0 and v[1] ==0.0 and v[0] ==0.0:
        return True
    else : return False

def proj_C(x):
    v = np.copy(x)
    if v[2] <=0.0:
        return np.array([0,0,v[2]])
    else:
        return np.array([0,0,0])

def CPA(x0,niter):
    k=0
    x=x0
    x_values=[x0]
    dist_c=[np.linalg.norm(proj_C(x0) - x0)]
    while k<niter:
        if k%2 ==0:
            x = proj_v2(x)
        else :
            x = np.array(pe.projprimalexpcone(x)[0])
        x_values.append(x)
        dist_c.append(np.linalg.norm(proj_C(x) - x))
        k+=1
    return x_values,dist_c

def dampDR_double_eta(x0,eta_prox,eta_v2,lbd,niter):
    k=0
    x=x0
    x_values=[x0]
    dist_c=[np.linalg.norm(proj_C(x0) - x0)]
    while k<niter:
        if isinC(x) : return x_values,dist_c
        y = (1/(2*eta_v2+1))*(x + 2*eta_v2*np.array(proj_v2(x)))
        z = (1/(2*eta_prox+1))*(2*y-x + 2*eta_prox*np.array(pe.projprimalexpcone(2*y-x)[0]))
        x = x + 2*lbd*(z-y)
        x_values.append(x)
        dist_c.append(np.linalg.norm(proj_C(x) - x))
        k+=1
    return x_values,dist_c

def DR(x0,niter):
    k=0
    x=x0
    x_values=[x0]
    y_values=[]
    dist_c=[np.linalg.norm(proj_C(x0) - x0)]
    dist_c_y=[]
    while k<niter:
        if isinC(x) : return x_values,dist_c
        y = 2*np.array(pe.projprimalexpcone(x)[0]) - np.array(x)
        z = 2*np.array(proj_v2(y)) - np.array(y)
        x = 0.8*x + 0.2*z
        x_values.append(x)
        y_values.append(y)
        dist_c.append(np.linalg.norm(proj_C(x) - x))
        dist_c_y.append(np.linalg.norm(proj_C(y) - y))
        k+=1
    return x_values,dist_c,y_values,dist_c_y