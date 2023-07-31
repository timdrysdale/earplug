#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:02:43 2023

@author: tim
"""

import numpy as np
import matplotlib.pyplot as plt

# See Section 6.1 Theory of Optical Coatings in Springer Handbook of Lasers & Optics
# Traeger (Ed)
# https://link.springer.com/referenceworkentry/10.1007/978-0-387-30420-5_6

# earplug thickness
thickness = 15e-3 #15mm

v_air = 330 #m/s
v_plug = 1110 #m/s See Ba. et al. 2017 https://hal.science/hal-02901486
n0 = v_air / v_air
n1 = v_plug / v_air
n2 = v_air / v_air
f = np.logspace(0,5,num=10000)
wavelength = v_air / f
theta_incident = 0 #radians

d1= 2*np.pi*n1*thickness*np.cos(theta_incident)/wavelength

r1=(n0-n1)/(n0+n1)
r2=(n1-n2)/(n1+n2)

rrcos = 2*r1*r2*np.cos(2*d1)

Rs = (r1**2 + rrcos + r2**2)/(1 + rrcos + (r1**2)*(r2**2))

logRs = 10*np.log10(Rs)

plt.plot(f/1e3,logRs)
plt.xlim([0,40])
plt.ylim([-50, 1])
plt.xlabel("freq (kHz)")
plt.ylabel("intensity (dB)")

overall = 10*np.log10(np.sum(Rs)/len(Rs))
plt.annotate("overall %0.1f dB"%(overall), (5,-45))

plt.title("transmission of a lossless ear-plug (1D model)")
plt.savefig("./img/lossless-1d-%dmm.png"%(thickness*1e3), dpi=300)

# lossly case
alpha = 30 * (f/1e6)**1.4 #(see Ba et al 2017)
plt.figure()
rrcos = 2*r1*r2*np.cos(2*d1)*np.exp(alpha*thickness)
Rs = (r1**2 + rrcos + r2**2)/(1 + rrcos + (r1**2)*(r2**2))

logRs = 10*np.log10(Rs)

plt.plot(f/1e3,logRs)
plt.xlim([0,40])
plt.ylim([-50, 1])
plt.xlabel("freq (kHz)")
plt.ylabel("intensity (dB)")

overall = 10*np.log10(np.sum(Rs)/len(Rs))
plt.annotate("overall %0.1f dB"%(overall), (5,-45))

plt.title("transmission of a lossy ear-plug (1D model)")
plt.savefig("./img/lossy-1d-%dmm.png"%(thickness*1e3), dpi=300)
