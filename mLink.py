import numpy as np



def PDF(rho,POVM):
    total=np.trace(np.matmul(POVM,rho))
    return np.real(total)

def unityTrace(rho):
    return rho/np.trace(rho)

def Rop(rho,proj,F):
    R= np.array([[0.+0.j,0.+0.j],[0.+0.j,0.+0.j]])
    N=np.size(F)
    for i in np.arange(0,N):
        prob=np.real(PDF(rho,proj[i]))
        if  prob!=0:
            R+=proj[i]*F[i]/prob
    
    return R
    
    

def maxlink(rho,proj,F,N):
    # rho is aseed density matrix
    # proj is an array of projectors 
    # F is an array of probabilities of getting eigenvalue of project proj[i]
    # N is number of iteration for maxLink algorithm
    for i in np.arange(0,N):
        Rop1 = Rop(rho,proj,F)
        rho = unityTrace(np.dot(np.dot(Rop1,rho),Rop1))
        rho = unityTrace(rho)       
    return rho

def getData(str1):
    arr = np.genfromtxt(str1, delimiter=";", dtype=np.single)
    Click1=np.count_nonzero(arr[:,1] == 2.)
    Click2=np.count_nonzero(arr[:,1] == 1.)
    return [Click1,Click2]