#!

# suppress warning outputs for using lal in jupuyter notebook
import warnings
warnings.filterwarnings("ignore", "Wswiglal-redir-stdio")

import GWFish.modules as gw
from tqdm import tqdm
import matplotlib
import matplotlib.pyplot as plt
import corner
import numpy as np
import pandas as pd
import json
import os
from astropy.cosmology import Planck18

# Parameters over a range of masses and tidal deformabilities of BNS

mc = np.linspace(0.5,5,10)
q = np.linspace(0.5,1,10)
lam1 = np.linspace(50,1000,10)
lam2 = np.linspace(50,1000,10)

parameters = {
    'chirp_mass': np.array([1.1858999987203738]) * (1 + 0.00980),
    'mass_ratio': np.array([0.8308538032620448]),
    'luminosity_distance': Planck18.luminosity_distance(0.00980).value,
    'theta_jn': np.array([2.545065595974997]),
    'ra': np.array([3.4461599999999994]),
    'dec': np.array([-0.4080839999999999]),
    'psi': np.array([0.]),
    'phase': np.array([0.]),
    'geocent_time': np.array([1187008882.4]),
    'a_1':np.array([0.005136138323169717]),
    'a_2':np.array([0.003235146993487445]),
    'lambda_1': np.array([368.17802383555687]),
    'lambda_2': np.array([586.5487031450857])}
parameters = pd.DataFrame(parameters)

print(parameters)

