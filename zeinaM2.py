import numpy as np
import matplotlib.pyplot as plt 
import sounddevice as sd
import math
from scipy.fftpack import fft

f=[293.66 , 440, 293.66, 329.63, 349.23, 392, 349.23, 329.63]
F=[146.83, 174.61, 174.61,  146.83, 146.83, 146.83, 164.81, 164.81]

t=[0,0.5,1,1.5,1.6,1.7,2,2.5]
T=[0.5,0.5,0.5,0.1,0.1,0.1,0.3,0.5]
tl = np. linspace(0 , 3 , 12 * 1024)


def u(t):
    return 1*(t>=0)
x=0

for i in range(0,7):
    u1=np.reshape([tl>=t[i]],np.shape(tl))*1
    u2=np.reshape([tl>T[i]],np.shape(tl))*1
    equation=(np.sin(2*np.pi*f[i]*tl)+np.sin(2*np.pi*F[i]*tl))*(np.reshape((u1-u2),np.shape(tl)))
   
    
    x=x+equation



N = 3*1024
f = np.linspace(0, 512, int(N/2))
xf = fft(x)
xf = 2/N * np.abs( xf [0:np.int(N/2)])
fn1,fn2= np.random.randint(0, 512, 2)
Noise = np.sin(2*fn1*np.pi*tl)+np.sin(2*fn2*np.pi*tl)
xn = x+Noise
xx= fft(xn)
xx= 2/N * np.abs(xx [0:np.int(N/2)])


max1=max(xn)

rest=[]

for j in range(0, len(xn)):
    if(xn[j]!=max1):
        rest.append(xn[i])

max2=max(rest)
index1=0
index2=0
for k in range(0,len(xf)):
      if(xf[k]==max1):
          index1=k
      if(xf[k]==max2):
          index2=k
          
freq1= round(f[index1])
freq2=round(f[index2])
xFil= xn  - np.sin(2*freq1*np.pi*tl)+np.sin(2*freq2*np.pi*tl)
result = fft(x)
result= 2/N * np.abs(xFil[0:np.int(N/2)])
plt.subplot(6,2,1)
plt.plot(tl,x)
plt.subplot(6,2,2)
plt.plot(f,xf)
plt.subplot(6,2,3)
plt.plot(tl,xn)
plt.subplot(6,2,4)
plt.plot(f,xx)
plt.subplot(6,2,5)
plt.plot(tl,xFil)
plt.subplot(6,2,6)
plt.plot(f,result)



sd.play(xFil,3*1024)       


