"""
Created on Fri Aug  9 00:37:56 2024

@author: ANAND
"""

import sys
import numpy as np
import control as ct

# KS is btwn 1 and 20

def LQRchargecurve(DepTime, EAmount, KS):
    # system matrices
    A=np.array([[0]])
    B=np.array([[1]])
    C=np.array([[1]])
    D=np.array([[0]])
     
    #define the initial condition
    x0=np.array([[0]])
   
    # define the time vector for simulation
    startTime=0
    endTime = round(DepTime/60)*60
    numberSamples = round(endTime/60)
    timeVector=np.linspace(startTime,endTime,numberSamples)
    #print('TimeVector!: ', timeVector)
   
    # state weighting matrix
    Q=KS/1000
     
    # input weighting matrix
    R=KS*1000

    # system matrices

    sysStateSpace=ct.ss(A,B,C,D)
    xd=np.array([[EAmount]])

    K, S, E = ct.lqr(sysStateSpace, Q, R)

    Acl=A-np.matmul(B,K)
    Bcl=-Acl
     
    # define the state-space model
    sysStateSpaceCl=ct.ss(Acl,Bcl,C,D)
     
    # define the input for closed-loop simulation
    inputCL=np.zeros(shape=(1,numberSamples))
    inputCL[0,:]=xd*np.ones(numberSamples)
    returnSimulationCL = ct.forced_response(sysStateSpaceCl,
                                          timeVector,
                                          inputCL,
                                          x0)
   

    # YC is state of charge of the vehicle (progress to eamount)
    # UC is power
    # TC is the timevector 
    Yc = returnSimulationCL.states[0,:]
    Uc=  np.transpose(-K*(returnSimulationCL.states[0,:]-inputCL))
    Tc = returnSimulationCL.time

    #print('YC is: ', Yc)
    #print('UC is: ', Uc)

    return Yc, Uc


def main():
    if len(sys.argv) != 3:
        print("Usage: python preview.py <date_time> <deamount> <ks>")
        return
    departure_time = sys.argv[1]
    eamount = sys.argv[2]
    ks = sys.argv[3]
    print("About to run LQR!")
    yc, uc = LQRchargecurve(departure_time, eamount, ks)


if __name__ == "__main__":
    main()






