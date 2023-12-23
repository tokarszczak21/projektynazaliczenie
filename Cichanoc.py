import sounddevice as sd
import numpy as np
from numpy import  pi, sin

frequency = 440
fs = 48000
seconds = 3
dt = 1/fs

t1 = np.arange(0,2,dt)
t25 = np.arange(0,1.5,dt)
t2 = np.arange(0,1 ,dt)
t45 = np.arange(0,2/3,dt)
t4 = np.arange(0, 1/2 ,dt)
t8 = np.arange(0, 1/4 ,dt)
t16 = np.arange(0, 1/8 ,dt)
note  = np.sin(2 * pi * frequency * t8)

fgm = 196.00;
fam = 220.00;
fhm = 246.94;
fc1 = 261.63;
fd1 = 293.66;
fe1 = 329.63;
ffis1 = 369.99;
fg1 = 392.00;
fa1 = 440.00;
fh1 = 493.88;
fc2 = 523.25;


xgm1=sin(2*pi*fgm*t1)
xam4=sin(2*pi*fam*t4)
xhm25=sin(2*pi*fhm*t25)
xhm2=sin(2*pi*fhm*t2)
xhm45=sin(2*pi*fhm*t45)
xhm4=sin(2*pi*fhm*t4)
xc18=sin(2*pi*fc1*t8)
xd125=sin(2*pi*fd1*t25)
xd145=sin(2*pi*fd1*t45)
xd14=sin(2*pi*fd1*t4)
xd18=sin(2*pi*fd1*t8)
xe12=sin(2*pi*fe1*t2)
xe14=sin(2*pi*fe1*t4)
xe18=sin(2*pi*fe1*t8)
xfis12=sin(2*pi*ffis1*t2)
xfis14=sin(2*pi*ffis1*t4)
xfis18=sin(2*pi*ffis1*t8)
xg125=sin(2*pi*fg1*t25)
xg12=sin(2*pi*fg1*t2)
xg145=sin(2*pi*fg1*t45)
xg14=sin(2*pi*fg1*t4)
xa12=sin(2*pi*fa1*t2)
xa14=sin(2*pi*fa1*t4)
xa18=sin(2*pi*fa1*t8)
xh125=sin(2*pi*fh1*t25)
xc245=sin(2*pi*fc2*t45)

#oznaczenia liczbowe i literowe po nazwach literowych dźwięków to oznaczenia oktaw 
x=np.concatenate((xd145,xe18,xd14,xhm45,xd145,xe18,xd14,xhm45,xa12,xa14,xfis12,xfis14,xg12,xg14,xd125,xe12,xe14,xg145,xfis18,xe14,xd145,xe18,xd14,xhm2,xhm4,xe12,xe14,xg145,xfis18,xe14,xd145,xe18,xd14,xhm2,xhm4,xa12,xa14,xc245,xa18,xfis14,xg125,xh125,xg145,xd18,xhm4,xd145,xc18,xam4,xgm1))
sd.play(x, fs)
