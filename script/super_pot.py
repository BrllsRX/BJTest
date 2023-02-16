import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

from comsol_pot import load_comsol_FEM, load_comsol_pot
from exp_volts import get_exp_volts
from util import arb_linear_interp


data_path = r'..\source\01_TFApprox_test\itr_gate_pot'
FEM_grid = load_comsol_FEM(data_path)
exp_volt = get_exp_volts()

# allocate pd for components of potential
ele_pot = pd.DataFrame(columns=exp_volt.keys())
for gate, vol in exp_volt.items():
    # apply real experimental voltage
    ele_pot[gate] = load_comsol_pot(data_path, gate=gate)*vol
    
# superpose potentials
pot_2deg = ele_pot.sum(axis=1)

# interpolate FEM results
X = np.arange(-1000, 1000, 1)
Y = np.arange(-2000, 2000, 1)
xx, yy = np.meshgrid(X, Y)
grid_pot = griddata(np.array(FEM_grid), np.array(pot_2deg), (xx, yy), method='nearest')

# plot false color potential of 2DEG
plt.imshow(grid_pot, origin='lower')

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(X, grid_pot[2000, :])
ax2 = fig.add_subplot(122, sharey=ax1)
ax2.plot(grid_pot[2000-150:2000+150, 1000])

SET_cut_x = np.array([1000, 2000-150, 2000+150, 3000])
SET_cut_y = np.array([1600, 1000,     1000,     1600])
npnts = np.array([500, 400, 500])

distance, SET_linecut = arb_linear_interp(SET_cut_x, SET_cut_y, npnts, grid_pot)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(distance, SET_linecut)

